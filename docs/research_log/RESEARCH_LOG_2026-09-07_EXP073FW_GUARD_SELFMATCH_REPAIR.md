# DSIR research log — 2026-09-07 — Exp073FW guard and orchestration repair

## Scope

Autoresearch guard inspection of the frozen DSIR4 heavy-chain transition from the admitted `WW_S1_S3` authority to the next permitted target `WW_S2_S2` (`Exp073FW`). This entry records infrastructure/orchestration events only and does not alter scientific logic, contracts, thresholds, hypothesis IDs, source ordering, exact-equality requirements, or the frozen domain.

## Last valid scientific predecessor

Run `34120000242` (`Exp073FU WW_S1_S3 autonomous audited home science v0.1`) is terminal `success`:

- hosted launch audit job `101735630917`: success;
- home-science job `101735669327`: success;
- hosted provenance admission job `101735763144`: success;
- admission log contains `PASS_EXP073FV_WW_S1_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, and `ww_s1_s3_authority_created=true`;
- the admitted predecessor dispatched `exp073fw-ww-s2-s2-home-science-v0-1.yml`.

Therefore `WW_S1_S3` is the last valid terminal authority and `WW_S2_S2` is the next frozen heavy target.

## Failure 1 — inherited guard self-match

Run `34121012410` (`Exp073FW WW_S2_S2 autonomous audited home science v0.1`):

- hosted-launch-audit job `101738782234`: success;
- home-science job `101738820469`: failure before scientific computation;
- hosted-provenance-admission job `101738894036`: skipped;
- failing diagnostic: `fail-closed tolerance/rescue path`.

Root cause: the FW wrapper transformed the inherited FM generator and then scanned the complete inherited generator source. The forbidden spellings were present only inside the inherited fail-closed scanner itself, so the outer scanner matched its own guard implementation rather than a scientific rescue path.

Classification: `INFRASTRUCTURE/IMPLEMENTATION_FAILURE`, scientific contribution `+0/+0`. No scientific terminal artifact was produced; this is not scientific FAIL.

## Repair 1

The outer lexical audit was restricted so the exact two inherited guard-implementation lines do not self-match, while any forbidden occurrence elsewhere remains fatal.

- repair commit: `09cf5b398d22286afab7715fbee450b114d4d065`;
- resulting home-wrapper blob: `331dee31602de5c5aa2ee1d3c2bf2241acce5cb3`;
- workflow binding commit: `e7129a3299f1e2f49ec3a1b4546a578a64fc9cf8`.

## Failure 2 — hosted marker drift

Run `34125359067`:

- hosted-launch-audit job `101752658903`: failure;
- home-science job `101752721363`: skipped;
- hosted-provenance-admission job `101752721863`: skipped.

The hosted static audit expected the explanatory literal `scanning its source text would self-match`; Repair 1 had reworded that comment. No self-hosted computation ran.

Classification: `INFRASTRUCTURE/IMPLEMENTATION_FAILURE`, scientific contribution `+0/+0`; not scientific FAIL.

## Repair 2

Restored the hosted-audit marker in a comment only.

- repair commit: `f1f29bf2fef56d52b3ce3f13645de22d8fb682d2`;
- resulting home-wrapper blob: `ffddbe96946e3f143be9f9334c24b23d75e00498`;
- workflow binding commit: `2fa1a9e50700ef921b3735c80324fbf412740e60`.

## Failure 3 — recursive transformed-shell syntax failure

Run `34125530921`:

- hosted-launch-audit job `101753205410`: success;
- home-science job `101753245014`: failure;
- hosted-provenance-admission job `101753313010`: skipped.

The self-hosted log fails immediately after generation of the transformed shell:

- `continue: only meaningful in a for, while, or until loop`;
- `syntax error near unexpected token '('`.

No Exp073FW computation started and the evidence upload reported no files. This demonstrates an orchestration/generator syntax defect rather than a scientific result.

Classification: `INFRASTRUCTURE/IMPLEMENTATION_FAILURE`, scientific contribution `+0/+0`; not scientific FAIL.

## Repair 3 — direct frozen FA-base transformation

Following the already validated architecture used by the admitted FU recovery, the FW home wrapper now transforms the frozen FA base directly instead of recursively executing the FM generator. The transformation remains prospectively fixed to the already-frozen FW identities:

- experiment namespace `exp073fa -> exp073fw`;
- target `ww_s0_s2 -> ww_s2_s2`;
- source pair `S0->S2 -> S2->S2`;
- ordered indices `[0,2] -> [2,2]`;
- driver identities remain `exp073fw_ww_s2_s2_durable_ab_production_v0_{1,2}.py`;
- terminal path remains A then prune, B then prune, exact terminal-receipt comparator;
- inherited storage-audit helper blobs are bound as infrastructure provenance only;
- `bash -n` is mandatory before executing the generated shell.

No thresholds, equations, hypothesis IDs, source ordering, contract fingerprint, domain limits, or exact-equality criteria were changed.

- direct-base repair commit: `820b0f8c082e45b2f51c3ff9d076a197ee3848f2`;
- resulting home-wrapper blob: `c4ef9587d5f4b54179304a44741eece2cec0a7a5`;
- workflow binding / hosted-audit adaptation commit: `1c635f5192d26e76e0ec82a308363b666e5a248b`.

## Current recovery run

Run `34125785882` was created from binding commit `1c635f5192d26e76e0ec82a308363b666e5a248b`.

At the most recent checkpoint recorded in this log, hosted-launch-audit job `101754018941` was running. No duplicate heavy run was intentionally launched. The concurrency group remains fail-closed with `cancel-in-progress: false`.

## Scientific status

- `WW_S1_S3`: `SCIENTIFIC_AUTHORITY_ADMITTED` from run `34120000242`.
- `WW_S2_S2`: `NOT_YET_ADMITTED` until a valid terminal artifact passes Exp073FX provenance admission.
- Scientific FAIL introduced by this repair cycle: **0**.
- Infrastructure/implementation failures in this repair cycle: **3**, all before scientific terminal scoring.

Taxonomy remains unchanged: infrastructure failure, `INVALID_FOR_SCIENCE`, `NOT_YET_TESTABLE`, and `OUTSIDE_DOMAIN` must never be promoted or translated into scientific FAIL.
