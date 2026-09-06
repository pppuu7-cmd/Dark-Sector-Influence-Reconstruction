# DSIR current-process ledger

Updated: 2026-09-06
Scope: DSIR only; RTK/RQIR excluded.

## Preserved/admitted authority
Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 exact scientific PASS remain preserved. `WW_S0_S0` is now admitted scientific authority by Exp073EO v0.2 run/job `34005373819 / 101411448176`, artifact `9980754356`, digest `sha256:0e1a4cff3b761fecc65d8e07df9e56f8109fd221fb4454746caa8c7d0f2fb4be`, token `PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_2`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, `ww_s0_s0_authority_created=true`.

Historical Exp073EO v0.1 NumPy runtime failure and string-vs-int EM artifact-ID provenance block remain `+0/+0`. Historical Exp073EY first hosted preflight failure `34006121336 / 101413506204` remains provenance/infrastructure `+0/+0`; its home job `101413524265` was skipped and no EY numerical science ran under the bad EL digest binding.

## Verified WW_S0_S1 resource readiness
Exp073EL run `34005467421`, hosted job `101411738320`, home job `101411728725`, artifact `9980783193`, authoritative live and independently recomputed ZIP digest `sha256:c720233664be2e8a7666db6f95def0a2f13eb674732add6852f0c09e916e5e46`, raw token `PASS_EXP073EL_WW_S0_S1_FULLRES_RESOURCE_PATH_V0_2`, classification `FULLRES_RESOURCE_PATH_READY`, accounting `+0/+0`. Earlier `f66da690...` digest was a stale provenance transcription and is not authority.

## Authoritative current process — Exp073EY WW_S0_S1
Workflow: `Exp073EY WW_S0_S1 file-backed A/B science v0.1`.

- run `34006214398`;
- hosted authority-preflight job `101413770925`: SUCCESS;
- self-hosted home-science job `101413789646`: **IN_PROGRESS** at latest reconciliation;
- activation/head SHA `0476ce61a84a97392abb80afadad188a588bbe1f`;
- science workflow blob `e6711cecea8e30122a1477215d68e8559ae9b832`;
- frozen source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- science prereg blob `5790f7502370abffc5c450278520cc73c1f901f8`;
- implementation prereg blob `a2ea3a705a4cb6f32c8b5337ce522cb7b72b0737`;
- identity erratum blob `748b6c2ad0f2a1cb4508d2607e65a2ad88c636b9`;
- EL-binding erratum blob `716e4c0e9054af79029e53923992776dbc6e3850`;
- ordered distinct source pair `(S0,S1)`;
- DES NSIDE=4096, ell `0..12287`, 39 bands;
- selected semantics `EE<-EE = wins[0,:,0,:]`, canonical `<f8 [39,12288]`;
- exact-only A/B SHA256 plus `numpy.array_equal`, finiteness, no tolerance rescue;
- public `read_from(..., read_unbinned_MCM=True) -> get_bandpower_windows()` route with exact 19,327,352,832-byte regular-file `/proc/self/maps` proof;
- checkpoint namespace A: `checkpoints/exp073ey-ww-s0-s1-a-v0-1`;
- checkpoint namespace B: `checkpoints/exp073ey-ww-s0-s1-b-v0-1`;
- stage order: `fresh_sources_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_ee_complete -> replica_receipt_complete`.

Static qualification is closed: `34006046818 / 101413292411` token `PASS_EXP073EY_STATIC_FAILCLOSED_AUDIT_V0_1`; `34006100427 / 101413444610` token `PASS_EXP073EY_STATIC_FAILCLOSED_AUDIT_V0_2`; corrected-binding audit `34006195574 / 101413721477` token `PASS_EXP073EY_STATIC_FAILCLOSED_AUDIT_V0_3`.

**Runner ownership:** DSIR-HOME-PC is reserved exclusively for Exp073EY `34006214398 / 101413789646`. Never launch a competing self-hosted DSIR run.

**Last durable checkpoint:** intentionally not inferred from partial live numerical state. Partial output is not inspected for adaptive decisions.

**On terminal SUCCESS:** download and independently hash the compact artifact; verify frozen source/contract/driver/workflow identities, both complete ordered six-stage checkpoint chains, ordered distinct-field proof, file-backed public-BPW proof, exact A/B selected SHA/array equality, finiteness and terminal token. A valid PASS is `WW_S0_S1` candidate pending a separately frozen provenance-admission gate; do not create authority from workflow SUCCESS alone.

**On valid completed exact A/B mismatch:** classify genuine `WW_S0_S1` scientific FAIL and move to the next allowed branch without tuning the gate.

**On infrastructure/resource/provenance/checkpoint failure:** identify the first cause, preserve all valid complete stages and resume from the last verified checkpoint; accounting `+0/+0`; never weaken science.

Frozen frontier: `Wm_S1 -> Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.
