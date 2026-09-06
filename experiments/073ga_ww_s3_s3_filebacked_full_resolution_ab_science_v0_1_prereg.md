# Exp073GA — WW_S3_S3 file-backed full-resolution A/B science v0.1

Prospectively frozen 2026-09-06 for the final WW angular authority target.

Entry: may start only after `WW_S2_S3` admission token `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.

Frozen target: `WW_S3_S3`, indices `[3,3]`, source pair `S3->S3`; reconstruct authoritative S3 exactly once per replica; construct exactly one spin-2 `NmtField`; pass the same Python field object to both coupling sides `compute_coupling_matrix(f3,f3,...)`; equal-but-distinct second field forbidden.

DES/NaMaster contract: NSIDE=4096; ell `0..12287`; 39 bands; public file-backed NaMaster 2.7 serialized-workspace route; full BPW `[4,39,4,12288]`; selected canonical `<f8 [39,12288]`, `wins[0,:,0,:]=EE<-EE`; exact `/proc/self/maps` proof; MCM backing exactly `19,327,352,832` bytes.

S3 authority: selected `4,196,641`; bytes `16,786,564`; record SHA `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec`; unique `2,943,132`; occupancy SHA `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094`.

Common source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; R1 artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`; NaMaster head `24365fa59a38c15732f4f37e8b29265b75c442d5`; patch blob `d534b698f9131688d263eedcef27260386c58641`.

A/B replicas use disjoint six-stage checkpoints, complete-chain verification before pruning, terminal comparison without replica restore, exact SHA equality, `numpy.array_equal`, and all-finite requirement.

PASS token: `PASS_EXP073GA_WW_S3_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`. Candidate creates no authority; final `Exp073GB` provenance admission required. Exact mismatch is scientific FAIL. No tolerance/allclose/isclose/rounding/smoothing/averaging/manual reconstruction/effective-coordinate/fiducial-P rescue. Downstream 14-window/radial/covariance/relation scoring remains forbidden until final WW admission closes.
