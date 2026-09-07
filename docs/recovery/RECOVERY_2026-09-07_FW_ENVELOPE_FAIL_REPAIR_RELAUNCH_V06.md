# DSIR immutable recovery — Exp073FW envelope failure / prospective repair / relaunch

Date: 2026-09-07. Scope: DSIR only.

## Preserved authority

`WW_S1_S3` remains admitted only by Exp073FV run `34120000242`, job `101735763144`. No later event changes that authority.

## Historical Exp073FW attempt 1

Run `34120059297`, head `d45bf07026956e0bbd95da4f0bfb5840393390e1`:
- hosted launch audit job `101735824056`: SUCCESS;
- home job `101735874893` on `DSIR-HOME-PC-2`: FAILURE before FW science started;
- provenance admission `101735934811`: SKIPPED;
- evidence upload found no files because no FW checkpoint root was created.

First causal failure from the raw home log:
`fail-closed missing FW home invariant "'source_pair':'S2->S2'"`.

This is an implementation/static-envelope failure `+0/+0`, not a scientific or numerical `WW_S2_S2` failure. The frozen driver had already passed hosted checks for `source_count_map(r1_root,2)`, ordered `[2,2]`, and `compute_coupling_matrix(f2,f2,b)`. The defect was that the outer shell transform incorrectly demanded serialized driver literals inside a shell envelope that never contains those literals.

## Prospective smallest repair

Commit `2bc804f641568a2517f903c0417a351889213219`, repaired home-wrapper blob `3c7e64e9a359ced198c2cb56b9a7c93f6c54c3d1`.

Repair scope only:
- remove impossible outer-shell requirements for `source_pair` and `ordered_source_indices`;
- audit those exact frozen identities directly in `ci/exp073fw_ww_s2_s2_durable_ab_production_v0_1.py` instead;
- retain stale FM-token rejection and no-tolerance/rescue audit.

Scientific arithmetic, source domain, thresholds, field semantics, exactness requirements and provenance contract are unchanged.

Workflow binding/one-shot activation commit `e71180515487fef117fe52f51fe9fdee983613df` binds `HOME_BLOB=3c7e64e...` and adds hosted audit checks for the direct frozen-driver identity.

## Relaunch

Repaired Exp073FW run `34120560190`, head `e71180515487fef117fe52f51fe9fdee983613df`, was launched by the scoped workflow-path push. At this note, hosted audit job `101737385038` is in progress. No competing queued/in-progress DSIR heavy process existed immediately before launch.

Exact next action: consume hosted audit; if it passes, allow exactly one home job to own `DSIR-HOME-PC-2`; on terminal home result consume raw logs/artifact and classify under the frozen `WW_S2_S2` contract. If the home job fails for infrastructure/software reasons, preserve any complete durable checkpoints and repair only the first causal defect. Scientific authority may be created only by the frozen Exp073FX admission gate after a validated FW candidate.
