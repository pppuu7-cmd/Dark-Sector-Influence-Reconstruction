# Exp073FU — WW_S1_S3 file-backed full-resolution A/B science v0.1

Date frozen: 2026-09-06. Scope: DSIR Article-3 angular authority.

## Entry condition
This heavy target may start only after `WW_S1_S2` is independently admitted with exact token `PASS_EXP073FT_WW_S1_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1`. Missing/failed predecessor admission blocks launch.

## Frozen target
- ordered target `WW_S1_S3`; source indices `[1,3]`; source pair `S1->S3`; reversed order forbidden.
- reconstruct S1 exactly once and S3 exactly once per replica.
- construct exactly two distinct spin-2 `NmtField` objects; same-object handoff forbidden.
- coupling order `compute_coupling_matrix(f1,f3,...)`.
- DES NSIDE=4096; ell `0..12287`; 39 bands.
- public file-backed NaMaster 2.7: serialized workspace `read_from(...,read_unbinned_MCM=True)` then public `get_bandpower_windows()`.
- full BPW `[4,39,4,12288]`; canonical selected `<f8 [39,12288]`, `wins[0,:,0,:] = EE<-EE`.
- exact file-backed MCM `/proc/self/maps` proof and backing bytes `19,327,352,832`.

## Frozen source authorities
S1: selected `7,851,711`; bytes `31,406,844`; record SHA256 `752f585125e413c7bd40cc5174cf7ef98e95f970022a351c5d91206f371d2241`; unique pixels `4,339,193`; occupancy SHA256 `fed1ffdf2ef7a7ae88e42615bd08e207e039239c44fa20b7994258f147a739f1`.

S3: selected `4,196,641`; bytes `16,786,564`; record SHA256 `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec`; unique pixels `2,943,132`; occupancy SHA256 `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094`.

Common source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; R1 artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`; NaMaster head `24365fa59a38c15732f4f37e8b29265b75c442d5`; patch blob `d534b698f9131688d263eedcef27260386c58641`.

## Durable A/B and scoring
Use disjoint A/B namespaces and the same six completed-stage manifests as the admitted cross-field architecture. Verify all complete-stage/payload hashes before pruning. Terminal comparison consumes only bound terminal/prune evidence plus canonical selected EE arrays and may not restore a completed replica.

Candidate PASS requires both replica full-chain verification, exact selected SHA256 equality, `numpy.array_equal`, all finite, exact ordered `[1,3]` distinct-field semantics, public file-backed route, exact MCM backing proof, no historical WW numerical import, and no other-replica numerical reads.

PASS token: `PASS_EXP073FU_WW_S1_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`. Candidate PASS creates no authority; separate Exp073FV admission is mandatory.

Forbidden: tolerance/allclose/isclose, rounding, smoothing, averaging, manual BPW reconstruction, effective-coordinate/fiducial-P shortcuts, reversed order, same-field reuse, or downstream join/radial/covariance/relation scoring.
