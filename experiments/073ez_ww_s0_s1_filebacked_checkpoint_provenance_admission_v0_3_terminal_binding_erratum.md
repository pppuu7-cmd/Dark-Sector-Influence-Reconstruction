# Exp073EZ — WW_S0_S1 provenance admission v0.3 terminal-binding erratum

Date: 2026-09-06. Scope: DSIR only; RTK/RQIR excluded.

This erratum is created only after authoritative Exp073EY checkpoint-resume run `34010599584`, home job `101425638857`, became terminal SUCCESS and its raw artifact was independently consumed. It binds terminal provenance only. It does not alter the immutable scientific or checkpoint acceptance rules of Exp073EZ v0.1, nor the prospective resume execution binding of v0.2.

## Immutable admission authority retained

Base science/provenance preregistration:
- `experiments/073ez_ww_s0_s1_filebacked_checkpoint_provenance_admission_v0_1_prereg.md`
- blob `346bdbedcb34bdd67a0df88e5444f08071e822b6`.

Resume-binding erratum:
- `experiments/073ez_ww_s0_s1_filebacked_checkpoint_provenance_admission_v0_2_resume_binding_erratum.md`
- blob `c5125bb9a09f6c02a1d6b48a862902ead9127b61`.

The only authority-writing token remains exactly:
`PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.

## Terminal candidate binding

The candidate-producing execution is exactly:
- workflow run `34010599584`;
- hosted repair-audit job `101425618749` = SUCCESS;
- home science-resume job `101425638857` = SUCCESS;
- activation/head `4c570bf6b7f3f53547f43e2882149defa125da89`;
- artifact ID `9983630139`;
- artifact name `exp073ey-ww-s0-s1-filebacked-ab-resume-v0-2`;
- GitHub artifact digest `sha256:12291c1c9f6100ebfb03a6db1e613f422bd48bc6c02720f89ee613c8646cf9d6`;
- independently downloaded ZIP SHA256 `12291c1c9f6100ebfb03a6db1e613f422bd48bc6c02720f89ee613c8646cf9d6`.

The artifact's terminal receipt is candidate-only, not authority. It reports exact token `PASS_EXP073EY_WW_S0_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`, classification `SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION`, `ww_s0_s1_authority_created=false`, source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, ordered indices `[0,1]`, source pair `S0->S1`, `same_field_object_handoff=false`, selected semantics `EE<-EE`, canonical dtype `<f8`, shape `[39,12288]`, exact A/B selected SHA256 `49af7a3d165daaf7cc6781e2286e45cd5baa0042ed9770800588bced7d700e79`, `numpy_array_equal=true`, all finite, and no tolerance rescue.

Both replica receipts bind full public BPW SHA256 `eb6c2427c86e76225a39feab3a4788d3a0b7ba142809f79cecb2e362c0b44b98`, full shape `[4,39,4,12288]`, route `public_get_bandpower_windows_after_filebacked_fits_read`, `read_unbinned_MCM=true`, regular-file-backed MCM size exactly `19327352832` bytes, live `/proc/self/maps` proof, and selected `wins[0,:,0,:] = EE<-EE`.

Both checkpoint namespaces contain the complete ordered six-stage chain required by v0.1:
`fresh_sources_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_ee_complete -> replica_receipt_complete`.
All retained manifests are `complete=true`, bind the same frozen source/contract identities, have `historical_ww_numerical_import=false` and `other_replica_output_read=false`. Replica A's first three expensive stages predate the resume and were restored under the frozen driver's exact identity/SHA checks; later A stages and replica B were completed by the resume. Post-receipt pruning occurred only after immutable receipt creation and selected-payload SHA verification.

## Admission rule

Exp073EZ activation must download artifact `9983630139` itself, independently recompute the ZIP SHA256, verify all v0.1 + v0.2 + this v0.3 bindings and raw payload/manifests, recompute selected A/B SHA256, load canonical `<f8 [39,12288]` arrays, require `numpy.array_equal`, finiteness, exact ordered `(S0,S1)` semantics, full six-stage chains, exact mmap/public-BPW provenance and the frozen candidate token. Workflow success alone is insufficient.

Any mismatch is fail-closed `BLOCKED_EXP073EZ_* +0/+0`; no WW authority may be created. Only an exact admission PASS may emit `PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1` with `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, `science_gate_scored=true`, `ww_s0_s1_authority_created=true`.

Status after this binding: `READY_FOR_HOSTED_ADMISSION`; WW_S0_S1 authority is still false until the admission run passes.