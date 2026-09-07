# DSIR4 autoresearch guard — Exp073FW post-compute pruner-token repair

Date: 2026-09-07
Target: `WW_S2_S2` (`Exp073FW` producer, `Exp073FX` provenance admission)

## Observed failure

Run `34125785882` (head `1c635f5192d26e76e0ec82a308363b666e5a248b`) reached the frozen self-hosted `WW_S2_S2` A/B producer after a successful hosted launch audit.

- hosted-launch-audit job `101754018941`: SUCCESS.
- home-science job `101754061309`: FAILURE.
- hosted-provenance-admission job `101785905987`: SKIPPED because the producer did not reach a successful terminal state.
- partial/compact evidence artifact: id `10023848524`, artifact ZIP digest `sha256:33b5999213247a9ad0c66957a021067f4f790f04d19eb1cf8d88910187eea66f`.

The self-hosted log shows `PASS_EXP073FW_LIVE_EXCLUSIVITY`, successful exact file-backed storage support checks, then a real heavy Replica A computation. The failure occurred only at the post-compute verify/prune boundary:

`RuntimeError: fail-closed missing FW pruner token 'WW_S1_S1'`

## Root cause and classification

`ci/exp073fw_verify_and_prune_replica_v0_1.py` transforms the frozen `Exp073FM` pruner. It incorrectly required an uppercase lexical token `WW_S1_S1`. The pinned FM base (`8e04e99084aed582f9586e3f316c023650ce6c63`) contains no such uppercase token. Its actual frozen identities are represented by `ww_s1_s1`, `ww-s1-s1`, `S1->S1`, `[1,1]`, `s1_count_map`, and corresponding receipt/schema invariants.

Therefore this is an **INFRASTRUCTURE/IMPLEMENTATION_FAILURE +0/+0**, not a scientific failure. No `WW_S2_S2` scientific authority was created, and the target remains `NOT_YET_ADMITTED`.

The heavy Replica A work must not be repeated merely because its subsequent lexical transformer failed. Durable checkpoints are authoritative only after the repaired verifier validates their existing hash/receipt chain; otherwise the system remains fail-closed.

## Repair

The repair removes only the nonexistent uppercase token from the mandatory lexical-transform list while preserving all actual frozen-token requirements, transformed invariants, stale-token rejection, source geometry, source ordering, exact hash checks, exact-equality semantics, file-backed route, contract fingerprint, thresholds, and hypothesis identities.

- pruner repair commit: `2a6a06f9d468879ca814ced15a56f82169507b3a`
- repaired pruner blob: `fb66e67d88a90b093a7da8b42ab0ac6fee13b504`
- workflow binding commit: `f7e925e782983824b7e916ce8437fcf924ec5760`
- bound workflow blob: `c7c651dfeac8a9d4a2d3da1dd6b11d7873af612a`

No frozen scientific logic, contract fingerprint, threshold, source pair, source indices, hypothesis ID, or comparator criterion was changed.

## Recovery chain

The workflow-file binding push started exactly one recovery run:

- recovery run `34135965569`, head `f7e925e782983824b7e916ce8437fcf924ec5760`.
- hosted-launch-audit job `101786894169`: SUCCESS.
- home-science job `101786993129`: IN_PROGRESS at the time of this log entry.

Repository-wide Actions inspection at recovery start showed this as the only in-progress workflow and no competing/duplicate `Exp073FW` heavy run. No extra manual heavy dispatch was made.

The recovery policy is checkpoint-first: validate and reuse already-created durable stages/Replica A evidence where valid; compute only missing work required by the frozen producer; do not infer scientific PASS/FAIL from partial checkpoints. `Exp073FX` may classify the science only after a complete terminal artifact passes provenance admission.

## Scientific status

- predecessor `WW_S1_S3`: `SCIENTIFIC_AUTHORITY_ADMITTED` (unchanged authority).
- current `WW_S2_S2`: `NOT_YET_ADMITTED`.
- this repair: `SUPPORT/INFRASTRUCTURE +0/+0`.
- new scientific FAIL from this incident: **0**.
- `INVALID_FOR_SCIENCE`, `NOT_YET_TESTABLE`, `OUTSIDE_DOMAIN`, and infrastructure failures remain distinct from scientific FAIL by policy.
