# Exp073FG — WW_S0_S3 file-backed full-resolution A/B science v0.1 preregistration

Prepared prospectively after Exp073FF admitted `WW_S0_S2`. Scope: DSIR only; RTK/RQIR excluded.

Upstream required: Exp073FF run/job `34032384956 / 101484177968`, exact token `PASS_EXP073FF_WW_S0_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1`; frozen source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; R1 artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`.

Frozen ordered pair is exactly `(S0,S3)`, authoritative R1 indices `[0,3]`; never `(S3,S0)` and never same-field. Reconstruct both source maps independently from authoritative R1 records; create two distinct spin-2 fields; compute exact ordered coupling matrix.

Frozen numerical/storage semantics are unchanged from the admitted WW architecture: DES NSIDE=4096; ell `0..12287`; 39 bands; serialized workspace `read_from(..., read_unbinned_MCM=True)` followed by public `get_bandpower_windows()`; regular-file-backed unbinned MCM exactly `19,327,352,832` bytes with `/proc/self/maps` proof; full BPW `[4,39,4,12288]`; selected `EE<-EE = wins[0,:,0,:]`, canonical `<f8 [39,12288]`; exact A/B SHA equality plus `numpy.array_equal`; all finite; no tolerance/allclose/rounding/smoothing/averaging/manual reconstruction/effective-coordinate/fiducial rescue.

Durable namespaces: `checkpoints/exp073fg-ww-s0-s3-a-v0-1` and `checkpoints/exp073fg-ww-s0-s3-b-v0-1`. Required six-stage chain per replica: `fresh_sources_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_ee_complete -> replica_receipt_complete`. Complete-stage restore must fail closed on frozen identities and payload hashes. Use exactly 8 outer workers only where the unit decomposition is scientifically identical and nested BLAS/OpenMP/MKL/OpenBLAS/NumExpr threads are pinned to 1; do not change arithmetic for performance.

Historical WW numerical payload import is forbidden. `other_replica_output_read=false` until terminal comparison. Exact A/B mismatch is genuine scientific FAIL. Candidate PASS token is prospectively frozen as `PASS_EXP073FG_WW_S0_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`, classification `SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION`; candidate alone creates no authority. A separate provenance admission is mandatory before `WW_S0_S3` authority exists.

Status: `PREREGISTERED_NOT_ACTIVATED`. Before any home heavy run, a hosted prerequisite/static audit must verify S3 R1 authority, admitted S0/S2 predecessor, frozen identities, checkpoint/restore architecture and absence of tolerance/rescue paths.
