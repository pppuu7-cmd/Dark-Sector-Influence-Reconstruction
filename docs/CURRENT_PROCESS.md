# DSIR current-process ledger

Updated: 2026-09-06
Scope: DSIR only; RTK/RQIR excluded.

## Preserved authority
Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 exact scientific PASS remain preserved. Historical negative/resource/infrastructure results remain immutable. Current scientific target is `WW_S0_S0`.

## Exp073EN — terminal scientific candidate PASS pending admission
Authoritative file-backed A/B run `33994398927`, self-hosted job `101382229273`, activation head `4d1cbd504067a64a94b038292793e5e8bffba911` is terminal SUCCESS. Raw terminal artifact `9980311204` has GitHub digest and independently recomputed ZIP SHA256 `54db5c1c213a041616111071c23ce2710e88c0f085efc9e625dd51538e71dd49`.

Raw evidence passes the frozen candidate checks: source `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; full A/B six-stage chains; file-backed MCM proof; selected canonical `<f8 [39,12288]` `EE<-EE`; exact A/B selected SHA256 `244f8f831ac7041af00f9cddca0ea93a04298fb0b1b029af5030376ce93da647`; bytewise equality and frozen `numpy.array_equal=true`; terminal token `PASS_EXP073EN_WW_S0_S0_FILEBACKED_AB_EXACT_REPEATABILITY_8CORE_V0_1`; no tolerance rescue. Exp073EN classification is `SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION`; it does not itself create `WW_S0_S0` authority.

DSIR-HOME-PC is released from Exp073EN ownership. No new self-hosted DSIR workload has been launched.

## Exp073EO v0.1 historical runtime/provenance blocks
Initial real hosted admission run/job `34005282438 / 101411204812` passed metadata and EN ZIP binding, then failed before auditor execution because NumPy was absent. Classification: infrastructure runtime dependency `+0/+0`, not science FAIL. Runtime-only repair pinned `numpy==2.3.3`.

Second real run/job `34005304226 / 101411264696` reached the frozen auditor and fail-closed `BLOCKED_EXP073EO_PROVENANCE_ADMISSION_V0_1`, reason `RuntimeError: terminal EM identity`. Root cause is a representation-only defect: authoritative EN stores hosted Exp073EM artifact ID as JSON string `"9977333691"`; v0.1 auditor constant was integer `9977333691`. Value and digest are identical. This remains provenance/software BLOCKED `+0/+0`, never scientific FAIL.

## Authoritative current process — Exp073EO v0.2
Prospectively frozen representation-only repair prereg: `experiments/073eo_ww_s0_s0_filebacked_checkpoint_provenance_admission_v0_2_prereg.md`, blob `2f8e615d75d1b920c6d2f2d5c831fed08a7b2a22`. Auditor wrapper `ci/exp073eo_ww_s0_s0_provenance_admission_v0_2.py`, blob `62e71d2541f0e94677b4ecaf3f3184fca15fe3c0`, reuses the frozen v0.1 auditor blob `4403d3e140acd14f0b95a31a8b2851f3229c1da3` and changes only `EM_ID` representation to exact string `"9977333691"`; all scientific/provenance/hash/checkpoint/storage gates remain unchanged. Real consumer blob `d28aa333767866d1c0c3a7230e246ca29b1bd1cc`.

Current hosted run/job: `34005373819 / 101411448176`, activation head `d848a081a4c2344c4e58af26360ddaaee8147ffd`, state **IN_PROGRESS** at latest reconciliation. Expected terminal PASS token: `PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_2`.

On PASS: inspect raw EO v0.2 receipt/artifact; only exact admission PASS creates `WW_S0_S0` scientific authority. Then, with no self-hosted owner, activate the already prospectively frozen Exp073EL v0.2 host resource admission gate. On BLOCKED/infrastructure failure: diagnose the first cause and preserve Exp073EN candidate evidence unchanged. On genuine qualified scientific repeatability FAIL only: preserve it as negative science.

## Future WW_S0_S1 readiness
Exp073EL v0.2 remains `PREREGISTERED_NOT_ACTIVATED` until real Exp073EO admission PASS. Its checker was statically qualified by Exp073EX; support chain EM/EK/EP/ER/EU/EV/EW remains `+0/+0`. After EO PASS, EL may run on DSIR-HOME-PC only when no competing self-hosted DSIR process owns the runner. EL resource PASS would still not score science; a separate full-resolution `WW_S0_S1` A/B scientific run must then be frozen and dispatched.

Frozen frontier: `Wm_S1 -> Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.
