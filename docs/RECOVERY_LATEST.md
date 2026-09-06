# DSIR authoritative recovery — latest

Updated: 2026-09-06. Scope: **DSIR only**. Never mix RTK or RQIR into this control/recovery plane.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 exact scientific PASS remain preserved. Historical negative, resource and infrastructure outcomes remain immutable and are never rewritten.

`WW_S0_S0` remains admitted by Exp073EO v0.2 run/job `34005373819 / 101411448176`, artifact `9980754356`, digest `sha256:0e1a4cff3b761fecc65d8e07df9e56f8109fd221fb4454746caa8c7d0f2fb4be`, token `PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_2`.

Exp073EL resource readiness remains support PASS `+0/+0`: artifact `9980783193`, digest `sha256:c720233664be2e8a7666db6f95def0a2f13eb674732add6852f0c09e916e5e46`.

## WW_S0_S1 — admitted

Authoritative candidate producer: Exp073EY checkpoint-resume run `34010599584`, hosted repair audit `101425618749` SUCCESS, home science job `101425638857` SUCCESS, head `4c570bf6b7f3f53547f43e2882149defa125da89`.

Candidate artifact `9983630139`, name `exp073ey-ww-s0-s1-filebacked-ab-resume-v0-2`, has GitHub digest and independently downloaded ZIP SHA256 exactly:
`12291c1c9f6100ebfb03a6db1e613f422bd48bc6c02720f89ee613c8646cf9d6`.

Raw candidate evidence passed the frozen exact gate:
- source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- ordered distinct `(S0,S1)`;
- both complete six-stage A/B chains under `checkpoints/exp073ey-ww-s0-s1-{a,b}-v0-1`;
- regular-file-backed MCM exactly `19,327,352,832` bytes with live `/proc/self/maps` proof;
- public `read_from(..., read_unbinned_MCM=True) -> get_bandpower_windows()` route;
- full BPW `[4,39,4,12288]`, SHA `eb6c2427c86e76225a39feab3a4788d3a0b7ba142809f79cecb2e362c0b44b98` for both replicas;
- selected canonical `<f8 [39,12288]` `EE<-EE`, A/B SHA `49af7a3d165daaf7cc6781e2286e45cd5baa0042ed9770800588bced7d700e79`;
- `numpy.array_equal=true`, all finite, no tolerance/rescue;
- candidate token `PASS_EXP073EY_WW_S0_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- candidate classification remained `SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION`, with no authority write.

Terminal-binding governance is frozen in `experiments/073ez_ww_s0_s1_filebacked_checkpoint_provenance_admission_v0_3_terminal_binding_erratum.md`, blob `d3c6c1ba9c6f6f4d41d1d123e765f8de5ead0fec`, commit `9b63c291d6c966166a70111e31fd39ab0c31b1d6`, layered on immutable Exp073EZ v0.1 prereg blob `346bdbedcb34bdd67a0df88e5444f08071e822b6` and prospective v0.2 resume-binding blob `c5125bb9a09f6c02a1d6b48a862902ead9127b61`.

Exp073EZ first hosted admission run/job `34017884048 / 101444857315` is historical `INFRASTRUCTURE_DEPENDENCY_FAIL +0/+0`: frozen identities and candidate artifact metadata/digest checks passed, then raw audit could not import NumPy. The smallest repair added only audit dependency `numpy==2.3.2`; no science/provenance criterion changed. Repair commit `a429b4a3b439bcca92e3adccfaa0de621137f6bc`.

Repaired Exp073EZ run/job **`34017921734 / 101444964371`** completed SUCCESS and raw log emitted exactly:
`PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`
with `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, `science_gate_scored=true`, `ww_s0_s1_authority_created=true`.
The hosted admission independently re-downloaded candidate artifact `9983630139`, reverified the ZIP SHA256, checked frozen blobs/run/jobs, both checkpoint chains, raw selected payload SHA, canonical exact array equality/finiteness, file-backed mmap/public-BPW provenance, live exclusivity evidence and post-receipt pruning. Therefore **WW_S0_S1 is admitted scientific authority**.

Immutable recovery note for this transition: `docs/recovery/RECOVERY_2026-09-06_EXP073EZ_ADMITTED_WW_S0_S1_EXP073FA_PREREG.md`, commit `7b4a39e70ad2b9cde20fc33e43c8eff69a0d3254`.

## Current frontier — WW_S0_S2

No queued or in-progress DSIR Actions existed immediately after Exp073EZ admission, so the next ordered WW pair was prospectively frozen as **Exp073FA `WW_S0_S2`**.

Preregistration:
- file `experiments/073fa_ww_s0_s2_filebacked_full_resolution_ab_science_v0_1_prereg.md`;
- commit `a1ce88850d037b408eb5f8cdd3275dbc7cf629b4`;
- blob `edc044792be8ac7b796c8469943924942ae91932`.

Exp073FA freezes ordered distinct `(S0,S2)` using authoritative `source_count_map(...,0)` and `source_count_map(...,2)`, DES NSIDE=4096, ell `0..12287`, 39 bands, two spin-2 fields, exact ordered coupling, public serialized-workspace BPW extraction, file-backed unbinned MCM exactly `19,327,352,832` bytes, full `[4,39,4,12288]`, selected `EE<-EE <f8 [39,12288]`, finiteness, exact A/B SHA equality plus `numpy.array_equal`, and no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial rescue.

Dedicated durable namespaces are:
- `checkpoints/exp073fa-ww-s0-s2-a-v0-1`;
- `checkpoints/exp073fa-ww-s0-s2-b-v0-1`.
Each replica must preserve `fresh_sources_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_ee_complete -> replica_receipt_complete` with fail-closed identity/payload verification and no historical WW numerical import or other-replica output read.

Candidate token is frozen as `PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`. Candidate PASS alone will not create authority; a separately frozen terminal provenance admission will be required.

## Current process

Hosted-only workflow `Exp073FA WW_S0_S2 prerequisite static audit v0.1` is authoritative:
- run `34018080500`;
- job `101445404866`;
- activation/head `d2c1d5abb857d636eac586851f477e0c868c3dc9`;
- static audit step has completed SUCCESS; terminal workflow state must still be reconciled before using its support token.

This hosted gate checks the exact FA prereg blob, authoritative task-runner/source-2 support, qualified read-patch identity, upstream Exp073EZ terminal SUCCESS and absence of a permissive tolerance path. Expected token: `PASS_EXP073FA_WW_S0_S2_PREREQUISITE_STATIC_AUDIT_V0_1`; classification support `+0/+0`, no WW authority.

**Runner ownership:** no self-hosted DSIR job currently owns `DSIR-HOME-PC`; Exp073FA science has not started and has no durable science checkpoint yet.

On terminal static PASS, freeze/implement the dedicated Exp073FA S0_S2 checkpointed production envelope, run a hosted fail-closed implementation audit, live-check self-hosted exclusivity, and then launch exactly one home A/B science process. Do not import S0_S1 numerical payloads and do not reuse their checkpoint namespaces.

## Frozen global science boundaries

Unless a later authoritative recovery note prospectively supersedes them: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.