# DSIR immutable recovery — Exp073EO admitted; Exp073EL verified; Exp073EY running

Date: 2026-09-06. Scope: DSIR only; RTK/RQIR excluded.

## Newly admitted science authority
Exp073EN run/job `33994398927 / 101382229273`, head `4d1cbd504067a64a94b038292793e5e8bffba911`, terminal artifact `9980311204`, independently verified ZIP/GitHub SHA256 `54db5c1c213a041616111071c23ce2710e88c0f085efc9e625dd51538e71dd49`, produced a valid `WW_S0_S0` scientific candidate. Both A/B replicas have complete six-stage durable chains and exact selected `EE<-EE <f8 [39,12288]` SHA256 `244f8f831ac7041af00f9cddca0ea93a04298fb0b1b029af5030376ce93da647`; byte equality and frozen `numpy.array_equal` both pass. Source `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, exact file-backed MCM geometry `19327352832` bytes / `49152` rows and no-tolerance policy are preserved.

Exp073EO v0.1 had two historical `+0/+0` blocks: run/job `34005282438 / 101411204812` lacked NumPy before auditor execution; run/job `34005304226 / 101411264696` then exposed a representation-only string-vs-int Exp073EM artifact-ID defect. Neither is scientific FAIL. The prospectively frozen v0.2 representation repair preserved all hashes/science/provenance gates.

Exp073EO v0.2 run/job `34005373819 / 101411448176`, head `d848a081a4c2344c4e58af26360ddaaee8147ffd`, artifact `9980754356`, independently verified digest `sha256:0e1a4cff3b761fecc65d8e07df9e56f8109fd221fb4454746caa8c7d0f2fb4be`, returned raw token `PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_2`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, `science_gate_scored=true`, `ww_s0_s0_authority_created=true`. **WW_S0_S0 is therefore admitted scientific authority.**

## Exp073EL resource gate
The already statically audited checker remained unchanged. Governance-only Exp073EL v0.3 bound the admitted EO-v0.2 authority. Run `34005467421`, hosted job `101411738320`, home job `101411728725`, terminal artifact `9980783193` passed with token `PASS_EXP073EL_WW_S0_S1_FULLRES_RESOURCE_PATH_V0_2`, raw `classification=FULLRES_RESOURCE_PATH_READY`, accounting `+0/+0`, `science_gate_scored=false`, `ww_s0_s1_authority_created=false`.

Important authority correction: live GitHub metadata and an independent download/recomputed ZIP hash agree that artifact `9980783193` digest is **`sha256:c720233664be2e8a7666db6f95def0a2f13eb674732add6852f0c09e916e5e46`**. Earlier draft value `f66da690...` was incorrect and must never be used except as historical provenance-error evidence. Raw resource receipt preserves exact 8-CPU affinity, WSL memory/swap floors and both >=50-GiB disk floors.

## Exp073EY WW_S0_S1 prospective science gate
Scientific prereg blob `5790f7502370abffc5c450278520cc73c1f901f8` freezes ordered distinct `(S0,S1)`, DES NSIDE=4096, ell `0..12287`, 39 bands, distinct spin-2 fields, exact `compute_coupling_matrix(f0,f1,b)`, public serialized-workspace `get_bandpower_windows()`, selected `wins[0,:,0,:] = EE<-EE`, canonical `<f8 [39,12288]`, exact A/B SHA + `numpy.array_equal`, finiteness and no tolerance/rounding/smoothing/averaging/effective-ell/fiducial rescue.

Dedicated durable checkpoint namespaces are `checkpoints/exp073ey-ww-s0-s1-a-v0-1` and `checkpoints/exp073ey-ww-s0-s1-b-v0-1`, each with ordered stages `fresh_sources_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_ee_complete -> replica_receipt_complete`.

Two pre-data implementation defects were caught and repaired prospectively: the first draft referenced the historical reconstruction adapter, so it was replaced by the qualified public BPW route; then a hidden `wsp.mcm` ownership proof was replaced by exact regular-file `19327352832`-byte + `/proc/self/maps` proof after `read_from(..., read_unbinned_MCM=True)`. No numerical EY run occurred before these repairs. Driver v0.1 blob `1db1eabbdba492c476cc61d3c4d71147aa688384`; v0.2 public-route wrapper blob `066847006b2ed9d712d2c22d3576a0d8887fa7bf`; home envelope blob `e48453e71970eecabdc6dec33facb26b77bb9e4e`.

A prereg blob typo was separately corrected before data by identity erratum blob `748b6c2ad0f2a1cb4508d2607e65a2ad88c636b9`. Static audit v0.1 run/job `34006046818 / 101413292411` emitted `PASS_EXP073EY_STATIC_FAILCLOSED_AUDIT_V0_1`; workflow-inclusive v0.2 audit `34006100427 / 101413444610` emitted `PASS_EXP073EY_STATIC_FAILCLOSED_AUDIT_V0_2`.

First science activation run `34006121336` failed in hosted preflight `101413506204`; home job `101413524265` was skipped, so no science/checkpoint computation occurred. First causal failure was the stale wrong EL artifact digest. This is immutable provenance/infrastructure `+0/+0`. Prospective EL-binding erratum blob `716e4c0e9054af79029e53923992776dbc6e3850` binds authoritative digest `c7202336...e5e46`; corrected science workflow blob `e6711cecea8e30122a1477215d68e8559ae9b832`. Corrected-binding static audit run/job `34006195574 / 101413721477` emitted `PASS_EXP073EY_STATIC_FAILCLOSED_AUDIT_V0_3`.

## Current process
Corrected Exp073EY activation head `0476ce61a84a97392abb80afadad188a588bbe1f`. Current run `34006214398`: hosted authority preflight job `101413770925` SUCCESS; self-hosted `home-science-ab` job **`101413789646` IN_PROGRESS** at latest reconciliation, inside frozen ordered S0->S1 A/B gate. **DSIR-HOME-PC is reserved exclusively by Exp073EY `34006214398 / 101413789646`.** No competing self-hosted DSIR task is permitted.

Partial numerical output has not been inspected and durable stage is intentionally not guessed. On terminal state, consume the compact artifact first. A valid exact A/B PASS is only a `WW_S0_S1` candidate and must receive separate provenance admission before authority. A valid completed exact A/B mismatch is scientific FAIL. Any runner/transport/dependency/storage/checkpoint/provenance problem remains `+0/+0`, must preserve complete checkpoints and resume without changing science.
