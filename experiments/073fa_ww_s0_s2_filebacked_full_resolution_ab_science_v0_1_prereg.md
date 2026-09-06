# Exp073FA — WW_S0_S2 file-backed full-resolution A/B science v0.1 preregistration

Date: 2026-09-06. Scope: DSIR only; RTK/RQIR excluded.

## Upstream authority

This gate is frozen only after Exp073EZ admitted `WW_S0_S1` with exact token `PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1` in run/job `34017921734 / 101444964371`. Historical Exp073EY candidate artifact remains `9983630139`, independently verified ZIP SHA256 `12291c1c9f6100ebfb03a6db1e613f422bd48bc6c02720f89ee613c8646cf9d6`.

The next frozen frontier is `WW_S0_S2`. No later WW pair may be scored before this pair reaches its repository-defined terminal disposition.

## Frozen scientific semantics

Exp073FA computes only ordered distinct pair `(S0,S2)` using the same admitted full-resolution WW semantics as the preceding exact pair:
- frozen source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- DES `NSIDE=4096`, `ell=0..12287`, 39 bands with the repository's frozen band edges;
- source maps reconstructed independently from authoritative R1 records using `source_count_map(r1_root,0)` and `source_count_map(r1_root,2)`; no S0_S1 numerical payload may be imported;
- two distinct spin-2 `NmtField` objects;
- exact ordered `compute_coupling_matrix(f0,f2,b)`;
- NaMaster/PyMaster 2.7 at the already frozen upstream source head and qualified storage-only patch;
- serialized workspace route only: `read_from(..., read_unbinned_MCM=True) -> get_bandpower_windows()`;
- one regular-file-backed unbinned MCM exactly `19,327,352,832` bytes, present in `/proc/self/maps` while mapped;
- full BPW shape exactly `[4,39,4,12288]`;
- selected `EE<-EE = wins[0,:,0,:]`;
- canonical selected array exactly `<f8 [39,12288]`;
- all values finite;
- two independent replicas A and B must have identical canonical selected SHA256 and `numpy.array_equal(A,B)==true`.

No tolerance, `allclose`, rounding, smoothing, averaging, effective-ell/k/z substitution, fiducial-P shortcut, same-field shadow, reversed `(S2,S0)` handoff, historical WW numerical import, or result-dependent rescue is permitted.

## Durable checkpoint contract

Self-hosted execution is forbidden unless both replicas use dedicated namespaces:
- `checkpoints/exp073fa-ww-s0-s2-a-v0-1`;
- `checkpoints/exp073fa-ww-s0-s2-b-v0-1`.

Each replica must preserve the exact ordered six-stage chain:
1. `fresh_sources_complete`;
2. `fresh_workspace_mcm_complete`;
3. `mcm_fits_verified`;
4. `full_window_complete`;
5. `selected_ee_complete`;
6. `replica_receipt_complete`.

Every manifest is fail-closed on schema, stage, `complete=true`, replica, namespace, source head, contract fingerprint, payload SHA256/shape/dtype/semantics, `historical_ww_numerical_import=false`, and `other_replica_output_read=false`. Complete stages may be restored only after exact identity and payload verification. A verified expensive stage must never be recomputed unnecessarily.

## Execution/resource contract

Any home run must be the sole self-hosted DSIR owner, use the admitted resource architecture, exactly 8 available outer CPU workers/affinity when applicable, and pin nested OpenBLAS/MKL/NumExpr threads to 1. Storage qualification must fail closed before science. No competing home job is allowed.

The file-backed patch is storage-only: it must preserve public PyMaster 2.7 BPW arithmetic exactly. It may change allocation/backing mechanics only, not scientific arithmetic.

## Classification

Candidate PASS token is frozen as:
`PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`.

A candidate PASS means only `SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION`; it does not itself create `WW_S0_S2` authority. A later separately frozen provenance admission must consume the terminal raw artifact and may be the only authority-writing gate.

If both replicas complete under the frozen contract and exact A/B selected arrays differ, classify as genuine `WW_S0_S2` scientific FAIL. Infrastructure/resource/checkpoint/provenance/transport failures are `+0/+0` or BLOCKED as appropriate and must preserve verified complete stages for minimal repair/resume.

Status at preregistration: `PREREGISTERED_NOT_ACTIVATED`; `ww_s0_s2_authority_created=false`.