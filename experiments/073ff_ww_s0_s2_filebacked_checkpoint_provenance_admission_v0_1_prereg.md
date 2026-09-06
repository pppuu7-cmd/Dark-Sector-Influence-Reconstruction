# Exp073FF — WW_S0_S2 file-backed checkpoint provenance admission v0.1 preregistration

Prepared prospectively on 2026-09-06 while authoritative Exp073FA home science job `34020756634 / 101452805620` is still IN_PROGRESS. Scope is DSIR only; RTK/RQIR are excluded.

Exp073FF is an admission/provenance gate only. It MUST NOT inspect or tune against partial Exp073FA numerical output, MUST NOT modify the Exp073FA scientific criterion, and MUST NOT infer scientific PASS from GitHub workflow success.

## Upstream authority required
Exp073FF may run only after Exp073FA has reached a terminal state and a compact candidate artifact exists. The candidate must bind the exact frozen Exp073FA authority and implementation identities recorded by the repository at activation, including:
- admitted upstream `WW_S0_S1` authority from Exp073EZ run/job `34017921734 / 101444964371`, token `PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`;
- frozen source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- Exp073FA science prereg blob `edc044792be8ac7b796c8469943924942ae91932`;
- authoritative ordered pair exactly `(S0,S2)` and R1 indices `[0,2]`;
- durable namespaces `checkpoints/exp073fa-ww-s0-s2-a-v0-1` and `checkpoints/exp073fa-ww-s0-s2-b-v0-1`;
- repaired Exp073FD workflow run `34020756634`, activation/head `894885b2c2b811954d1724c2733d2a810a486d70`;
- hosted Exp073FD envelope audit job `101452788638` terminal SUCCESS `+0/+0`;
- home science job `101452805620` as the sole authoritative Exp073FA producer;
- Exp073FC committed-driver-binding support PASS `34018341064 / 101446155067`, token `PASS_EXP073FC_EXP073FA_COMMITTED_DRIVER_BINDING_V0_1`;
- Exp073FE restore-hardening support PASS `34023325339 / 101459798149`, token `PASS_EXP073FE_EXP073FA_TERMINAL_COMPARE_RESTORE_HARDENING_V0_1`.

The terminal Exp073FA artifact ID and artifact digest are deliberately unknown here. They must be read from live GitHub metadata after terminal state and independently verified by downloading the ZIP and recomputing SHA256 before Exp073FF activation. Any mismatch is fail-closed `+0/+0`.

## Frozen scientific semantics to preserve
Exp073FF audits but does not alter the Exp073FA science gate:
- ordered distinct pair exactly `(S0,S2)`, never `(S2,S0)` and never a same-field shadow;
- DES NSIDE=4096; `ell=0..12287`; 39 bands;
- source maps reconstructed independently from authoritative R1 records for indices 0 and 2;
- two distinct spin-2 `NmtField` objects and exact ordered `compute_coupling_matrix(f0,f2,b)`;
- qualified serialized workspace route `read_from(..., read_unbinned_MCM=True) -> get_bandpower_windows()`;
- regular-file-backed unbinned MCM exactly `19,327,352,832` bytes and present in `/proc/self/maps` while mapped;
- full BPW shape exactly `[4,39,4,12288]`;
- selected `EE<-EE = wins[0,:,0,:]`, canonical `<f8 [39,12288]`;
- exact A/B SHA256 equality plus `numpy.array_equal(A,B)==true`, finiteness, and no tolerance/allclose/rounding/smoothing/averaging/effective-coordinate/fiducial rescue.

## Immutable checkpoint chain to audit
For replicas A and B independently, Exp073FF must validate the complete ordered six-stage durable chain without skipping a stage:
1. `fresh_sources_complete`;
2. `fresh_workspace_mcm_complete`;
3. `mcm_fits_verified`;
4. `full_window_complete`;
5. `selected_ee_complete`;
6. `replica_receipt_complete`.

Every retained manifest/receipt must fail closed on schema, stage name, `complete=true`, replica identity, checkpoint namespace, source authority, contract fingerprint, activation/head identity, payload SHA256, required shape/dtype/semantics, `historical_ww_numerical_import=false`, and `other_replica_output_read=false`. Exp073FE hardening is part of the provenance interpretation: terminal A/B comparison must not weaken full-chain restore requirements or silently substitute terminal-only validation for the frozen six-stage contract.

If post-receipt pruning removed a large workspace or MCM payload, Exp073FF may accept pruning only when retained immutable evidence proves the payload was fully verified before pruning. Missing pre-receipt evidence or unverifiable pruning is `BLOCKED +0/+0`, never a science rescue.

## Ordered distinct-field and storage provenance
Exp073FF must independently verify terminal evidence proving:
- ordered field indices `[0,2]` and `(S0,S2)` handoff;
- distinct source-map identities appropriate to S0 and S2;
- `same_field_object_handoff=false` and distinct field-object proof;
- no import of historical `WW_S0_S0` or `WW_S0_S1` numerical payload into the new computation;
- each newly computed full-resolution workspace used the qualified file-backed backend;
- exact backing-file size `19327352832` bytes and expected geometry;
- public BPW extraction from serialized/reloaded workspace state;
- exact 8-CPU execution contract with nested BLAS/OpenMP/MKL/OpenBLAS/NumExpr threading pinned to 1 where frozen;
- no competing self-hosted DSIR heavy ownership during the science run.

## Scientific candidate verification
Exp073FF must consume the terminal Exp073FA compact artifact itself rather than trusting workflow status. It must require the exact candidate token:
`PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`.

For a candidate PASS, independently verify:
- artifact metadata digest equals independently recomputed downloaded-ZIP SHA256;
- all frozen source/contract/prereg/driver/envelope/workflow identities;
- both complete ordered six-stage chains;
- exact selected payload files and canonical metadata;
- selected A SHA256 equals selected B SHA256;
- `numpy.array_equal(A,B)==true` on canonical `<f8 [39,12288]` arrays;
- all selected values finite;
- ordered distinct `(S0,S2)` and `EE<-EE` semantics;
- exact file-backed public-BPW route and cleanup/resource provenance;
- Exp073FE terminal-compare hardening evidence where applicable;
- no tolerance or alternative-path rescue.

Exp073FF must not regenerate a missing scientific payload, repair an A/B numerical mismatch, substitute historical output, or infer equality from closeness.

## Classification and authority write
Only if every frozen check passes may Exp073FF emit:
`PASS_EXP073FF_WW_S0_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1`
with `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, `science_gate_scored=true`, and `ww_s0_s2_authority_created=true`.

That token is the only authority-writing PASS for this gate. A GitHub SUCCESS without it is not scientific authority.

If terminal Exp073FA is a fully qualified completed exact A/B mismatch, that is a genuine `WW_S0_S2` scientific FAIL and Exp073FF must not convert it to PASS. Any missing/malformed artifact, digest mismatch, checkpoint/provenance/storage/source/contract identity defect, runner/transport/dependency problem, or incomplete terminal evidence is `BLOCKED_EXP073FF_* +0/+0`; no WW_S0_S2 authority is created.

## Downstream frontier
Only after `PASS_EXP073FF_WW_S0_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1` may the WW frontier advance beyond `WW_S0_S2`. Any later pair must be separately preregistered from repository authority and may not be activated before this admission.

Status at preregistration: `PREREGISTERED_NOT_ACTIVATED`; `ww_s0_s2_authority_created=false`.
