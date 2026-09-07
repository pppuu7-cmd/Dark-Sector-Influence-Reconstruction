# DSIR research log — 2026-09-07 — Exp073FU post-prune terminal resume repair

## Scope
Autoresearch guard recovery for frozen DSIR4 Exp073FU `WW_S1_S3`. This entry is infrastructure/provenance bookkeeping only. No frozen scientific equations, source pair, hypothesis ID, thresholds, acceptance logic, contract fingerprint, or domain definition are changed.

## Observed failures

### 1. Original terminal-comparator infrastructure failure
- Run: `34103803637`
- Self-hosted home-science job: `101684145754`
- State: heavy replicas A and B had reached complete verified post-receipt/prune state before terminal comparison.
- Failure site: terminal comparator wrapper.
- Error: fail-closed missing FU comparator transform `S1S2`.
- Classification: `INFRASTRUCTURE_IMPLEMENTATION_FAILURE`, accounting `+0/+0`; **not scientific FAIL**.
- Scientific state from this run: `NOT_YET_ADMITTED`; no Exp073FV authority created.

The comparator repair was committed as `d8997622b4ab1a3f865ec927e6daf592dec76e29`; repaired comparator git blob is `94a649dd9a9a10bb497f40fff6f866826f2076cf`. It transforms the actual frozen FS schema/namespace tokens (`ww_s1_s2`, `ww-s1-s2`) to S1S3 identities and retains fail-closed stale-token and no-tolerance-rescue checks.

### 2. First comparator-repair resume exposed post-prune resume defect
- Run: `34119424522`
- Head SHA: `73e3dadbbdd42738cb8c8993e823b7e962573be6`
- hosted-launch-audit job: `101733789200` — SUCCESS.
- home-science job: `101733824692` — FAILURE before any new heavy computation.
- uploaded compact evidence artifact: `10017582834`.
- Error: `RuntimeError: fail-closed missing complete-stage payload s1_count_map.npy` while entering replica A.
- Cause: the production resume path treated a deliberately post-receipt-pruned checkpoint as if all pre-prune heavyweight payloads must still exist. The frozen pruner intentionally deletes source maps/workspace/full-window only *after* complete-chain verification and writes `post_receipt_prune.json`; the terminal comparator is explicitly designed to verify the surviving stage-manifest SHA chain, terminal receipt, selected-EE payload and post-prune receipt.
- Classification: `INFRASTRUCTURE_RESUME_CONTRACT_FAILURE`, accounting `+0/+0`; **not scientific FAIL**. The failure occurred before a new science score and before provenance admission.

## Repair
Commit `d4ad8a195676719d5a053cd09bdab017fde79c1c` hardens `ci/exp073fu_home_filebacked_fullres_v0_1.sh` with a terminal-resume branch:
- if `post_receipt_prune.json` and the canonical `exact_route/selected_ee.bin` survive for a replica, do not call the heavy producer again;
- do not reconstruct or restore pruned source/workspace/full-window payloads;
- send the preserved evidence directly through the frozen fail-closed terminal comparator, which rechecks every stage-manifest SHA, receipt identity, selected payload SHA/shape/finiteness, provenance identities, A/B exact equality, and no-tolerance-rescue condition;
- if terminal evidence is absent, retain the original run → verify/prune path.

Workflow binding for one-shot validation is commit `7e9dae4346962199f07072c4e7bf6e96f08b5673`. This repair changes orchestration/resume semantics only; it does not change scientific arithmetic or acceptance criteria.

## Recovery run
- Run: `34119633828` (`Exp073FU WW_S1_S3 autonomous audited home science v0.1`)
- Head SHA: `7e9dae4346962199f07072c4e7bf6e96f08b5673`
- hosted-launch-audit job: `101734455269` — SUCCESS.
- home-science job: `101734496880` — QUEUED at this log checkpoint.
- No second Exp073FU/other heavy run was started by this guard.

## Scientific classification
At this checkpoint:
- `WW_S1_S3 = NOT_YET_ADMITTED`.
- `scientific FAIL = 0` for the failures above.
- Infrastructure/implementation accounting: `+0/+0`.
- Exp073FV provenance admission must succeed and emit both `PASS_EXP073FV_WW_S1_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1` and `ww_s1_s3_authority_created=true` before S1S3 can be treated as admitted scientific authority or dispatch `Exp073FW WW_S2_S2`.
- `INVALID_FOR_SCIENCE`, `NOT_YET_TESTABLE`, `OUTSIDE_DOMAIN`, and infrastructure failures remain non-scientific classifications by construction.
