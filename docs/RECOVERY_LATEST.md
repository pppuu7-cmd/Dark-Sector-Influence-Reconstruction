# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-06
**Scope:** DSIR only; RTK/RQIR excluded.

Repository state, immutable recovery notes, validated GitHub Actions raw logs/artifacts and durable checkpoints outrank chat wording. Historical outcomes remain immutable. Never upgrade support evidence into science authority. Never mix DSIR with RTK or RQIR.

## Preserved science authority and frontier
Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 exact scientific PASS remain preserved.

**WW_S0_S0 is now admitted scientific authority.** Exp073EO v0.2 run/job `34005373819 / 101411448176`, head `d848a081a4c2344c4e58af26360ddaaee8147ffd`, artifact `9980754356`, independently verified digest `sha256:0e1a4cff3b761fecc65d8e07df9e56f8109fd221fb4454746caa8c7d0f2fb4be`, raw token `PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_2`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, `science_gate_scored=true`, `ww_s0_s0_authority_created=true`.

Current science target is **WW_S0_S1**.

Frozen order:
`Wm_S1 -> Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.

## Exp073EN evidence preserved
Exp073EN full-resolution file-backed A/B run/job `33994398927 / 101382229273`, activation head `4d1cbd504067a64a94b038292793e5e8bffba911`, terminal artifact `9980311204`, independently verified ZIP/GitHub SHA256 `54db5c1c213a041616111071c23ce2710e88c0f085efc9e625dd51538e71dd49`, was a valid `SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION` for WW_S0_S0. Exact selected A/B `EE<-EE <f8 [39,12288]` SHA256 is `244f8f831ac7041af00f9cddca0ea93a04298fb0b1b029af5030376ce93da647`; byte equality and frozen `numpy.array_equal` both pass. Both replicas have the ordered six-stage chain `fresh_s0_mask_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_ee_complete -> replica_receipt_complete`. Source `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, NaMaster `24365fa59a38c15732f4f37e8b29265b75c442d5`, and exact file-backed MCM geometry `19,327,352,832` bytes / `49,152` rows remain frozen.

Exp073EO v0.1 historical failures remain `+0/+0`: `34005282438 / 101411204812` lacked NumPy before auditor execution; `34005304226 / 101411264696` then exposed only a JSON string-vs-int Exp073EM artifact-ID representation defect. The prospectively frozen EO v0.2 repair changed only that representation and retained all scientific/provenance/hash/checkpoint criteria.

## WW_S0_S1 resource authority boundary
Exp073EL resource admission run `34005467421`, hosted job `101411738320`, home job `101411728725`, artifact `9980783193` passed token `PASS_EXP073EL_WW_S0_S1_FULLRES_RESOURCE_PATH_V0_2`, raw `classification=FULLRES_RESOURCE_PATH_READY`, accounting `+0/+0`, `science_gate_scored=false`, `ww_s0_s1_authority_created=false`.

**Authoritative Exp073EL artifact digest is `sha256:c720233664be2e8a7666db6f95def0a2f13eb674732add6852f0c09e916e5e46`.** Live GitHub metadata and an independent downloaded-ZIP SHA256 recomputation agree exactly. Earlier draft digest `f66da690...` was a provenance transcription error and is not authority. EL confirms DSIR-HOME-PC resource readiness: 8 CPU affinity, WSL configured/observed memory and swap floors, >=50 GiB WSL and Windows C: disk floors, and real mmap sanity. EL itself scores no science.

Qualified support chain EM/EK/EP/ER/EU/EV/EW/EX remains support-only `+0/+0`; Exp073ET remains immutable formal support FAIL `+0/+0`. Historical manual/saved-FITS reconstruction routes remain non-authoritative. Direct public `get_bandpower_windows()` after qualified file-backed construction/read is the allowed S0->S1 production path.

## Exp073EY — current authoritative WW_S0_S1 science process
Scientific prereg: `experiments/073ey_ww_s0_s1_filebacked_full_resolution_ab_science_v0_1_prereg.md`, blob `5790f7502370abffc5c450278520cc73c1f901f8`.

Frozen science:
- ordered distinct source pair exactly `(S0,S1)`, never `(S1,S0)` and never a same-field shadow;
- DES NSIDE=4096; ell `0..12287`; 39 bands;
- distinct spin-2 `NmtField` objects and exact `compute_coupling_matrix(f0,f1,b)`;
- public serialized-workspace `read_from(..., read_unbinned_MCM=True) -> get_bandpower_windows()` route;
- file-backed proof via one regular `dsir-nmt-mcm-*` file exactly `19,327,352,832` bytes and its path present in `/proc/self/maps`;
- full BPW `[4,39,4,12288]`; selected `EE<-EE = wins[0,:,0,:]`; canonical `<f8 [39,12288]`;
- exact A/B SHA256 equality plus `numpy.array_equal`; finiteness; no tolerance/allclose/rounding/smoothing/averaging/effective-ell/fiducial rescue.

Implementation/provenance bindings:
- v0.1 driver blob `1db1eabbdba492c476cc61d3c4d71147aa688384`;
- public-route v0.2 wrapper blob `066847006b2ed9d712d2c22d3576a0d8887fa7bf`;
- home execution envelope blob `e48453e71970eecabdc6dec33facb26b77bb9e4e`;
- implementation prereg blob `a2ea3a705a4cb6f32c8b5337ce522cb7b72b0737`;
- prereg identity erratum blob `748b6c2ad0f2a1cb4508d2607e65a2ad88c636b9`;
- Exp073EL digest-binding erratum blob `716e4c0e9054af79029e53923992776dbc6e3850`;
- corrected science workflow blob `e6711cecea8e30122a1477215d68e8559ae9b832`.

Two implementation defects were caught **before any EY numerical execution** and repaired prospectively: the historical reconstruction adapter was removed in favor of the qualified public route; then hidden `wsp.mcm` inspection was replaced by regular-file + `/proc/self/maps` proof. A prereg blob typo was separately corrected before data. None changed the frozen scientific criterion.

Static qualification is exact and complete:
- `34006046818 / 101413292411`: `PASS_EXP073EY_STATIC_FAILCLOSED_AUDIT_V0_1`;
- `34006100427 / 101413444610`: `PASS_EXP073EY_STATIC_FAILCLOSED_AUDIT_V0_2`;
- corrected-binding `34006195574 / 101413721477`: `PASS_EXP073EY_STATIC_FAILCLOSED_AUDIT_V0_3`.

First EY science activation run `34006121336` failed only in hosted preflight `101413506204` because it carried the stale wrong EL artifact digest; home job `101413524265` was skipped. This is immutable provenance/infrastructure `+0/+0`, not WW_S0_S1 science. The sole binding defect was corrected prospectively and statically re-audited before home execution.

### Current process ledger
Corrected Exp073EY run **`34006214398`**, activation/head **`0476ce61a84a97392abb80afadad188a588bbe1f`**:
- hosted authority preflight job `101413770925`: SUCCESS;
- self-hosted home science job **`101413789646`: IN_PROGRESS** at latest reconciliation;
- checkpoint A namespace `checkpoints/exp073ey-ww-s0-s1-a-v0-1`;
- checkpoint B namespace `checkpoints/exp073ey-ww-s0-s1-b-v0-1`;
- stage order `fresh_sources_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_ee_complete -> replica_receipt_complete`.

**DSIR-HOME-PC is reserved exclusively for Exp073EY `34006214398 / 101413789646`. Never launch a competing self-hosted DSIR run.** Partial numerical output must not be inspected for adaptive decisions; current durable stage must not be guessed from a live job.

Expected candidate token: `PASS_EXP073EY_WW_S0_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`. A workflow SUCCESS alone is insufficient. A valid exact A/B PASS is only a WW_S0_S1 candidate pending separately frozen provenance admission. A valid completed exact A/B mismatch is genuine WW_S0_S1 scientific FAIL. Infrastructure/resource/provenance/checkpoint failures remain `+0/+0` and require causal repair/resume from the last verified checkpoint without changing science.

## Frozen science/execution boundaries
`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid-row `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

## Exact next gates
1. Do not duplicate or disturb Exp073EY `34006214398 / 101413789646`.
2. The instant EY becomes terminal, consume raw compact evidence in the same iteration: workflow/jobs, artifact digest plus independent ZIP SHA256, frozen source/contract/workflow/driver identities, both ordered six-stage checkpoint chains, distinct-field handoff proof, exact file-backed public-BPW proof, selected A/B SHA/array equality, finiteness and terminal token.
3. On valid candidate PASS, prospectively freeze and run a hosted provenance-admission gate. Only that separate admission may create WW_S0_S1 authority; then advance to `WW_S0_S2`.
4. On genuine completed exact A/B mismatch, record WW_S0_S1 scientific FAIL and continue to the next scientifically permitted branch without tuning the frozen gate.
5. On infrastructure/resource/provenance/checkpoint failure, identify the first causal defect, preserve all verified complete checkpoint stages, repair minimally and resume; never recompute a verified expensive stage unnecessarily.

Current immutable recovery note: `docs/recovery/RECOVERY_2026-09-06_EXP073EO_ADMITTED_EL_VERIFIED_EY_RUNNING.md`.
