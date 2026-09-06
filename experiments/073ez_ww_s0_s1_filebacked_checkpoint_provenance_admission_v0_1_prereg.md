# Exp073EZ — WW_S0_S1 file-backed checkpoint provenance admission v0.1 preregistration

Prepared prospectively on 2026-09-06 while authoritative Exp073EY WW_S0_S1 full-resolution A/B science run `34006214398 / 101413789646` is still in progress. Scope is DSIR only; RTK/RQIR are excluded.

Exp073EZ is an admission/provenance gate only. It MUST NOT inspect or tune against partial Exp073EY numerical output, MUST NOT modify the Exp073EY scientific criterion, and MUST NOT infer scientific PASS from GitHub workflow success.

## Upstream authority required
Exp073EZ may run only after Exp073EY has reached a terminal state and a compact candidate artifact exists. The candidate must bind the exact frozen Exp073EY authority and implementation identities recorded by the repository at activation, including:
- admitted upstream `WW_S0_S0` authority from Exp073EO v0.2 run/job `34005373819 / 101411448176`, artifact `9980754356`, digest `sha256:0e1a4cff3b761fecc65d8e07df9e56f8109fd221fb4454746caa8c7d0f2fb4be`;
- Exp073EL resource PASS run `34005467421`, hosted job `101411738320`, home job `101411728725`, artifact `9980783193`, authoritative digest `sha256:c720233664be2e8a7666db6f95def0a2f13eb674732add6852f0c09e916e5e46`;
- frozen source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- Exp073EY scientific prereg blob `5790f7502370abffc5c450278520cc73c1f901f8`;
- Exp073EY v0.1 driver blob `1db1eabbdba492c476cc61d3c4d71147aa688384`;
- qualified public-route wrapper blob `066847006b2ed9d712d2c22d3576a0d8887fa7bf`;
- home execution envelope blob `e48453e71970eecabdc6dec33facb26b77bb9e4e`;
- implementation prereg blob `a2ea3a705a4cb6f32c8b5337ce522cb7b72b0737`;
- identity erratum blob `748b6c2ad0f2a1cb4508d2607e65a2ad88c636b9`;
- authoritative Exp073EL digest-binding erratum blob `716e4c0e9054af79029e53923992776dbc6e3850`;
- corrected Exp073EY science workflow blob `e6711cecea8e30122a1477215d68e8559ae9b832`;
- activation/head `0476ce61a84a97392abb80afadad188a588bbe1f` and workflow run `34006214398`.

The terminal Exp073EY artifact ID and artifact digest are deliberately not guessed here. They must be read from live GitHub metadata after terminal state and independently verified by downloading the ZIP and recomputing SHA256 before Exp073EZ activation. Any mismatch is fail-closed `+0/+0`.

## Frozen scientific semantics to preserve
Exp073EZ audits but does not alter the Exp073EY science gate:
- ordered distinct pair exactly `(S0,S1)`, never `(S1,S0)` and never a same-field shadow;
- DES NSIDE=4096; `ell=0..12287`; 39 bands;
- two distinct spin-2 `NmtField` objects and exact ordered `compute_coupling_matrix(f0,f1,b)`;
- qualified serialized workspace route `read_from(..., read_unbinned_MCM=True) -> get_bandpower_windows()`;
- regular-file-backed unbinned MCM exactly `19,327,352,832` bytes with expected `49,152` rows and path present in `/proc/self/maps` while mapped;
- full BPW shape exactly `[4,39,4,12288]`;
- selected `EE<-EE = wins[0,:,0,:]`, canonical `<f8 [39,12288]`;
- exact A/B SHA256 equality plus `numpy.array_equal(A,B)==true`, finiteness, and no tolerance/allclose/rounding/smoothing/averaging/effective-ell/fiducial rescue.

## Immutable checkpoint chain to audit
For replicas A and B independently, Exp073EZ must validate the complete ordered six-stage durable chain without skipping a stage:
1. `fresh_sources_complete`;
2. `fresh_workspace_mcm_complete`;
3. `mcm_fits_verified`;
4. `full_window_complete`;
5. `selected_ee_complete`;
6. `replica_receipt_complete`.

Exact namespaces are:
- `checkpoints/exp073ey-ww-s0-s1-a-v0-1`;
- `checkpoints/exp073ey-ww-s0-s1-b-v0-1`.

Every retained manifest/receipt must fail closed on schema, stage name, `complete=true`, replica identity, checkpoint namespace, source authority, contract fingerprint, activation/head identity, payload SHA256, required shape/dtype/semantics, `historical_ww_numerical_import=false`, and `other_replica_output_read=false`. If post-receipt pruning removed a large workspace or MCM payload, Exp073EZ may accept that only when the retained immutable receipt proves the payload was fully verified before pruning. Missing pre-receipt evidence or unverifiable pruning is `BLOCKED +0/+0`, never a science rescue.

## Ordered distinct-field and storage provenance
Exp073EZ must independently verify terminal evidence proving:
- ordered field indices `[0,1]` and `(S0,S1)` handoff;
- distinct source-map SHA identities appropriate to S0 and S1;
- `same_field_object_handoff=false` and distinct field-object proof as frozen upstream;
- no import of Exp073EN/WW_S0_S0 numerical payload into the new WW_S0_S1 computation;
- each newly computed full-resolution workspace used the qualified file-backed backend;
- exact backing-file size `19327352832` bytes and exact expected geometry;
- public BPW extraction from the serialized/reloaded workspace state;
- no surviving temporary `dsir-nmt-mcm-*` file after replica process exit where cleanup is required by the frozen implementation;
- exact 8-CPU execution contract and nested BLAS/OpenMP/MKL/OpenBLAS/NumExpr constraints;
- no competing self-hosted DSIR heavy ownership during the science run.

## Scientific candidate verification
Exp073EZ must consume the terminal Exp073EY compact artifact itself rather than trusting workflow status. It must require the exact candidate token:
`PASS_EXP073EY_WW_S0_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`.

For a candidate PASS, independently verify:
- artifact metadata digest equals independently recomputed downloaded-ZIP SHA256;
- all frozen source/contract/prereg/driver/wrapper/envelope/workflow identities;
- both complete ordered six-stage chains;
- exact selected payload files and canonical metadata;
- selected A SHA256 equals selected B SHA256;
- `numpy.array_equal(A,B)==true` on canonical `<f8 [39,12288]` arrays;
- all selected values finite;
- ordered distinct `(S0,S1)` and `EE<-EE` semantics;
- exact file-backed public-BPW route and cleanup/resource provenance;
- no tolerance or alternative-path rescue.

Exp073EZ must not regenerate a missing scientific payload, repair an A/B numerical mismatch, substitute historical output, or infer equality from closeness.

## Classification and authority write
Only if every frozen check passes may Exp073EZ emit:
`PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`
with `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, `science_gate_scored=true`, and `ww_s0_s1_authority_created=true`.

That token is the only authority-writing PASS for this gate. A GitHub SUCCESS without it is not scientific authority.

If the terminal Exp073EY run is a fully qualified completed exact A/B mismatch, that is a genuine Exp073EY WW_S0_S1 scientific FAIL and Exp073EZ must not convert it to PASS. Exp073EZ may record/verify that negative result but has no repair authority over scientific arithmetic.

Any missing/malformed artifact, digest mismatch, checkpoint/provenance/storage/source/contract identity defect, runner/transport/dependency problem, or otherwise incomplete terminal evidence is `BLOCKED_EXP073EZ_* +0/+0`; no WW_S0_S1 authority is created.

## Downstream frontier
Only after `PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1` may the scientific frontier advance from `WW_S0_S1` to `WW_S0_S2`. Any future WW_S0_S2 preregistration must preserve the repository's frozen WW semantics and may not be activated before this admission.

Status at preregistration: `PREREGISTERED_NOT_ACTIVATED`; `ww_s0_s1_authority_created=false`.