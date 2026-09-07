# DSIR research log — 2026-09-07 — Exp073FU post-prune terminal resume repair

## Scope
Autoresearch guard recovery for frozen DSIR4 Exp073FU `WW_S1_S3`. Infrastructure/provenance bookkeeping only. No frozen scientific equations, source pair, hypothesis ID, thresholds, acceptance logic, contract fingerprint, or domain definition are changed.

## Failure chain and classification

### 1. Original terminal-comparator failure
- Run `34103803637`; self-hosted job `101684145754`.
- Heavy replicas A and B had completed and passed full-chain verification/prune before terminal comparison.
- Comparator stopped on `fail-closed missing FU comparator transform 'S1S2'`.
- Classification: `INFRASTRUCTURE_IMPLEMENTATION_FAILURE`, accounting `+0/+0`; **not scientific FAIL**; `WW_S1_S3=NOT_YET_ADMITTED`.

Repair commit `d8997622b4ab1a3f865ec927e6daf592dec76e29` changed only FS→FU comparator token plumbing, including actual frozen lower-case schema/namespace identities. No arithmetic, equality criterion, threshold, hypothesis ID, source pair, or contract changed.

### 2. Post-prune resume defect
- Run `34119424522`, head `73e3dadbbdd42738cb8c8993e823b7e962573be6`.
- hosted-launch-audit job `101733789200` — SUCCESS.
- home-science job `101733824692` — FAILURE before new heavy computation.
- Artifact `10017582834`.
- Error: `RuntimeError: fail-closed missing complete-stage payload s1_count_map.npy`.
- Cause: resume path re-entered the heavy producer after the frozen pruner had intentionally deleted source maps/workspace/full-window *after* complete-chain verification.
- Classification: `INFRASTRUCTURE_RESUME_CONTRACT_FAILURE`, `+0/+0`; **not scientific FAIL**.

Repair commit `d4ad8a195676719d5a053cd09bdab017fde79c1c` added fail-closed terminal resume from preserved `post_receipt_prune.json` + canonical `exact_route/selected_ee.bin`. It neither reconstructs pruned heavy payloads nor reruns a completed replica; the unchanged terminal comparator must revalidate stage-manifest SHAs, receipt identity, selected-EE SHA/shape/finiteness, provenance fields and exact A/B equality before science scoring.

### 3. Uppercase comparator marker defect exposed by successful post-prune resume
- Run `34119633828`, head `7e9dae4346962199f07072c4e7bf6e96f08b5673`.
- hosted-launch-audit job `101734455269` — SUCCESS.
- home-science job `101734496880` — FAILURE.
- Both `PASS_EXP073FU_A_POST_PRUNE_TERMINAL_RESUME_CANDIDATE_V0_1` and `PASS_EXP073FU_B_POST_PRUNE_TERMINAL_RESUME_CANDIDATE_V0_1` were emitted, proving the heavy producer was not re-entered for either completed replica.
- Comparator then stopped before scoring with `fail-closed missing FU comparator invariant 'PASS_EXP073FU_WW_S1_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1'`.
- Root cause: lower-case `ww_s1_s2` identities had been transformed, but the frozen base PASS/FAIL markers contain an additional uppercase `WW_S1_S2` token.
- Classification: `INFRASTRUCTURE_IMPLEMENTATION_FAILURE`, `+0/+0`; **not scientific FAIL**.

Comparator commit `02c80f565cc6e74fe35d85948e298645d1da5799` / blob `08e91910da2b510ef92ab705dbbe360f57506a31` adds only `WW_S1_S2 -> WW_S1_S3`, requires both transformed PASS and FAIL markers, and fail-closes if an uppercase stale S1S2 token survives. Scientific comparison remains exact SHA + `numpy.array_equal` + finiteness, with no tolerance/rescue path.

Workflow binding commit `9b3d18e8127e856d102fb00ef226674435311710` pins that repaired comparator blob and adds the corresponding hosted static assertion.

## Current recovery run
- Run `34119825716` (`Exp073FU WW_S1_S3 autonomous audited home science v0.1`).
- Head SHA `9b3d18e8127e856d102fb00ef226674435311710`.
- State at this checkpoint: `QUEUED` immediately after the repair-trigger commit.
- This is the only newly triggered FU recovery run from the final repair; no duplicate heavy-run was intentionally started.
- The terminal-resume wrapper is required to reuse the already verified/pruned A/B checkpoints; if those identities do not validate, it must fail closed rather than silently reinterpret partial evidence.

## Scientific status
- `WW_S1_S3 = NOT_YET_ADMITTED` until Exp073FV provenance admission succeeds.
- Scientific FAIL introduced by this repair chain: **0**.
- Infrastructure/implementation failures above: `+0/+0`.
- Do not promote comparator candidate PASS alone to authority. Admission requires `PASS_EXP073FV_WW_S1_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, and `ww_s1_s3_authority_created=true`.
- `INVALID_FOR_SCIENCE`, `NOT_YET_TESTABLE`, `OUTSIDE_DOMAIN`, and infrastructure failures remain distinct non-scientific classifications.
