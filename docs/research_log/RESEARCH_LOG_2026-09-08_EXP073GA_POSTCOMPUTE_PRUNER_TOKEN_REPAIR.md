# DSIR research log — Exp073GA post-compute pruner token repair

Date: 2026-09-08
Target: DSIR4 `WW_S3_S3 / Exp073GA`

## Observed failure

- Failed workflow run: `34189540992`
- Head SHA: `10e6fb67af7d6485fca3d1ecf2362e4622883417`
- Hosted launch-audit job: `101944582891` — SUCCESS
- Self-hosted `home-science` job: `101944608861` — FAILURE
- Hosted final provenance admission job: `101964415971` — SKIPPED
- Evidence artifact: `10043979600`, name `exp073ga-ww-s3-s3-filebacked-ab-v0-1`
- Artifact digest: `sha256:b859e658e1046c4d9905d589003a1d26aaf3e2601c51d9db361b48176226906a`

The self-hosted job reached the expensive file-backed Replica-A calculation and produced the 19,327,352,832-byte MCM, then failed in the post-compute verifier/pruner before scientific A/B admission with:

`RuntimeError: fail-closed missing GA pruner token 'WW_S1_S1'`

The frozen FM-base pruner does not contain the literal uppercase token `WW_S1_S1`; its actual frozen markers include `ww_s1_s1`, `ww-s1-s1`, `S1->S1`, `[1,1]`, `s1_count_map`, and `S1 source`. Therefore the uppercase-token requirement was a false implementation matcher, not a scientific condition.

## Classification

`INFRASTRUCTURE/IMPLEMENTATION_FAILURE +0/+0`

Scientific FAIL contribution: **0**.

This failure MUST NOT be converted into scientific FAIL, `OUTSIDE_DOMAIN`, or any physical exclusion. `WW_S3_S3` remains `NOT_YET_ADMITTED` until a terminal candidate passes the separate provenance admission.

## Prospective repair

Only the nonexistent uppercase-token guard was removed from `ci/exp073ga_verify_and_prune_replica_v0_1.py`.

- Repair commit: `f52fa856eb029c64f744926eecf55f506fcf1da5`
- Repaired pruner blob: `fc3e4d8444630e4b5a2dde0a052e1069b7887c01`
- Workflow rebind + hosted regression commit: `f6d8b429ac64643e7cb7766e0bfa2ab51abe751d`

The regression audit now explicitly verifies that the frozen FM source contains the real lower/formal markers and does **not** contain `WW_S1_S1`.

No frozen numerical driver, source ordering `[3,3]`, same-field semantics, exact A/B equality requirement, contract fingerprint, threshold, hypothesis ID, or scientific admission criterion was changed.

## Recovery state

Before recovery there were zero `in_progress` and zero queued workflows, so exactly one recovery chain was allowed.

Automatic recovery run:

- Run: `34197207582`
- Head SHA: `f6d8b429ac64643e7cb7766e0bfa2ab51abe751d`
- Hosted launch-audit job: `101967492875` — SUCCESS
- Self-hosted `home-science` job: `101967543808` — IN_PROGRESS at last inspection

No second heavy-run was dispatched. The workflow retains the same durable checkpoint namespace and is intended to reuse valid persisted stages rather than intentionally recompute them. In-progress job logs were not yet downloadable during this inspection, so checkpoint reuse is not claimed beyond what the frozen durable-checkpoint workflow contract guarantees; terminal evidence remains fail-closed.

## Scientific status after repair

- `WW_S2_S2 = SCIENTIFIC_AUTHORITY_ADMITTED`
- `WW_S2_S3 = SCIENTIFIC_AUTHORITY_ADMITTED`
- `WW_S3_S3 = NOT_YET_ADMITTED / ACTIVE_RECOVERY_GATE`
- New scientific FAIL: `0`

Next permitted scientific transition: terminal `Exp073GA` candidate -> `Exp073GB` provenance admission. Downstream 14-window join remains blocked until explicit `PASS_EXP073GB_WW_S3_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1` and `ww_s3_s3_authority_created=true`.