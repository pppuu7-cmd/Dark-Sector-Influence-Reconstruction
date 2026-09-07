# DSIR recovery — Exp073FM consumed, Exp073FR admitted, Exp073FS running

Date: 2026-09-07. Scope: **DSIR only**. RTK/RQIR excluded.

## Newly closed: Exp073FM WW_S1_S1 exact candidate

Exp073FM workflow/run `34050657030`, home job `101533574294`, head `f0caca0c3e812710e5958ee13348a150d045a7d8` is terminal SUCCESS and was consumed scientifically rather than inferred from workflow status.

Frozen candidate token: `PASS_EXP073FM_WW_S1_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`.

Artifact authority consumed:
- artifact ID `9998932628`, name `exp073fm-ww-s1-s1-filebacked-ab-v0-1`, size `7380196` bytes;
- independent ZIP SHA256 `db3aa00e060047f354c5374c78dba3808491cf61a1d810114d35b474badd49af`, matching GitHub digest;
- canonical A/B selected payloads are both `<f8 [39,12288]`, 3,833,856 bytes each, SHA256 `ff7215d5e523134e10ef4c9b512c6829d66fd63af33dc5655bd8e88dfd0c33ff`;
- both arrays are finite and exact byte-equal / `numpy.array_equal` true;
- raw log contains both complete six-stage/prune verification markers and exact file-backed MCM proof `19,327,352,832` bytes;
- frozen source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, FR prereg blob `aa08636426dd48142c3a3da7c032f1075a1be1f9` remain bound.

Classification: `SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION`. Candidate alone created no authority.

## Terminal consumer

Run `34065976761`, job `101578311604` independently re-fetched the terminal FM run/jobs/artifact, downloaded and hashed the ZIP, re-ran `ci/exp073fr_verify_fm_terminal_evidence_v0_1.py`, and emitted:

- `PASS_EXP073FM_TERMINAL_EVIDENCE_CONSUMED_FOR_CANONICAL_FR_V0_1`;
- `classification=SUPPORT_TERMINAL_EVIDENCE_CONSUMED_PLUS_0_PLUS_0`;
- `ww_s1_s1_authority_created=false`.

This is support `+0/+0`, not scientific authority.

## Newly admitted authority: Exp073FR WW_S1_S1

Canonical Exp073FR run `34067345251`, hosted job `101578330386`, head `f3e49041a5b869ddf22be8ca7a612901ec9f9458` independently re-fetched and reverified the frozen Exp073FM evidence and emitted:

- `PASS_EXP073FR_WW_S1_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`;
- `classification=SCIENTIFIC_AUTHORITY_ADMITTED`;
- `ww_s1_s1_authority_created=true`.

Therefore `WW_S1_S1` is now formally admitted scientific authority. This does not modify any frozen science boundary or historical result.

## Current authoritative process: Exp073FS WW_S1_S2

Exp073FR deterministically dispatched the prospectively frozen successor. Current live Actions reconciliation shows exactly one in-progress DSIR workflow and no competing heavy successor:

- workflow/run: Exp073FS `34067352681`;
- hosted launch job `101578350681`: SUCCESS with `PASS_EXP073FS_HOSTED_LAUNCH_AUDIT_V0_1`, classification `SUPPORT_PLUS_0_PLUS_0`;
- home job: `101578366531`;
- branch/head: `main` / `f3e49041a5b869ddf22be8ca7a612901ec9f9458`;
- start: `2026-09-06T23:36:14Z`;
- state: IN_PROGRESS in `Run frozen WW_S1_S2 A/B gate with durable checkpoints`;
- runner ownership: `DSIR-HOME-PC` belongs exclusively to job `101578366531`;
- science prereg blob `80c6af017b47d51db3f588221749fb152577b0e5`;
- successor admission prereg Exp073FT blob `072bdeae68e86312142e980fe2015f979e7b117f`;
- cache/checkpoint root `~/.cache/dsir/exp073fs-ww-s1-s2-filebacked-ab-v0-1/checkpoints/{A,B}`;
- expected candidate token `PASS_EXP073FS_WW_S1_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- ordered source pair is `[1,2] = S1->S2`, two distinct spin-2 fields; same-object handoff is forbidden for this cross-pair;
- exact MCM backing remains `19,327,352,832` bytes; public BPW; canonical selected `<f8 [39,12288] EE<-EE`; exact A/B equality only; no tolerance rescue.

Partial FS numerical output/checkpoints were not inspected while the run is active.

On terminal SUCCESS: consume the artifact and raw log in full, verify both complete stage chains, ordered S1/S2 semantics and distinct field IDs, frozen source/contract/implementation identities, exact mmap proof, finiteness and exact A/B equality. Only a valid exact candidate permits Exp073FT scientific provenance admission. The installed workflow performs the prospectively frozen hosted admission only after successful home science, and only its authority token may dispatch Exp073FU. On infrastructure/resource failure: diagnose the first causal defect and resume from verified complete-stage checkpoints without changing science. On exact numerical mismatch: record scientific FAIL; no rescue.
