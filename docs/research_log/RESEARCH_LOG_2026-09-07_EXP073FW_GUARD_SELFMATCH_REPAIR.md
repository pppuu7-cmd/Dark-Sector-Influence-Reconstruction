# DSIR research log — 2026-09-07 — Exp073FW guard self-match repair

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

- head SHA observed for the bound relaunch: `656dc15eb1999f3935b5b2dc3e6db74dda3cfe38`;
- hosted-launch-audit job `101738782234`: success;
- home-science job `101738820469`: failure before scientific computation;
- hosted-provenance-admission job `101738894036`: skipped;
- failing diagnostic: `fail-closed tolerance/rescue path`.

Root cause: `ci/exp073fw_home_filebacked_fullres_v0_1.sh` transformed the inherited FM wrapper and then lexically scanned the complete inherited generator source. That source legitimately contains the forbidden spellings (`np.allclose`, `np.isclose`, `*_rescue`) only inside its own fail-closed scanner. The outer FW guard therefore matched the guard implementation itself rather than a scientific tolerance/rescue path.

Classification: `INFRASTRUCTURE/IMPLEMENTATION_FAILURE`, scientific contribution `+0/+0`. No scientific terminal artifact was produced and this event MUST NOT be treated as scientific FAIL, INVALID_FOR_SCIENCE, or evidence against the hypothesis.

## Repair 1 — exact guard-line exclusion

Changed only the outer lexical audit in `ci/exp073fw_home_filebacked_fullres_v0_1.sh`:

- scientific transformations remain unchanged;
- frozen driver identities remain unchanged;
- forbidden rescue terms remain fatal everywhere except the exact two inherited lines that implement the inner fail-closed guard itself;
- the frozen driver and hosted audit retain their independent checks.

Repair commit: `09cf5b398d22286afab7715fbee450b114d4d065`.
Resulting home-wrapper blob: `331dee31602de5c5aa2ee1d3c2bf2241acce5cb3`.
Workflow binding commit: `e7129a3299f1e2f49ec3a1b4546a578a64fc9cf8`.

## Failure 2 — hosted marker drift

The binding triggered run `34125359067`:

- hosted-launch-audit job `101752658903`: failure;
- home-science job `101752721363`: skipped;
- hosted-provenance-admission job `101752721863`: skipped.

The failure occurred in the hosted static audit before self-hosted execution. During Repair 1 the explanatory comment containing the frozen audit marker `scanning its source text would self-match` had been reworded, while the workflow intentionally greps that literal. No scientific computation ran.

Classification: `INFRASTRUCTURE/IMPLEMENTATION_FAILURE`, scientific contribution `+0/+0`; not scientific FAIL.

## Repair 2 — restore hosted audit marker

Restored the required explanatory literal in the comment only; no executable scientific semantics changed.

Repair commit: `f1f29bf2fef56d52b3ce3f13645de22d8fb682d2`.
Resulting home-wrapper blob: `ffddbe96946e3f143be9f9334c24b23d75e00498`.
Workflow binding commit: `2fa1a9e50700ef921b3735c80324fbf412740e60`.

## Recovery run

Run `34125530921` was created from binding commit `2fa1a9e50700ef921b3735c80324fbf412740e60`.

At the checkpoint recorded here:

- hosted-launch-audit job `101753205410`: `SUCCESS`;
- home-science job `101753245014`: queued for the single self-hosted heavy slot;
- no duplicate active heavy-run was intentionally launched.

The recovery run is allowed to reuse any valid durable checkpoint state under the existing Exp073FW checkpoint root. No completed heavy stage should be recomputed merely because the orchestration wrapper was repaired.

## Scientific status

- `WW_S1_S3`: `SCIENTIFIC_AUTHORITY_ADMITTED` (predecessor authority from run `34120000242`).
- `WW_S2_S2`: `NOT_YET_ADMITTED` pending a valid terminal artifact and Exp073FX provenance admission.
- Scientific FAIL introduced by this repair cycle: **0**.
- Infrastructure/implementation failures in this repair cycle: **2**, both pre-science / orchestration-only.

Fail-closed taxonomy remains unchanged: infrastructure failure, `INVALID_FOR_SCIENCE`, `NOT_YET_TESTABLE`, and `OUTSIDE_DOMAIN` must never be promoted or translated into scientific FAIL.
