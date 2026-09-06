# Exp073FY — WW_S2_S3 file-backed full-resolution A/B science v0.1

Prospectively frozen 2026-09-06 for DSIR Article-3 angular authority.

Entry: may start only after `WW_S2_S2` admission token `PASS_EXP073FX_WW_S2_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.

Frozen target: ordered `WW_S2_S3`, indices `[2,3]`, source pair `S2->S3`; reversed order forbidden. Reconstruct S2 exactly once and S3 exactly once per replica; construct exactly two spin-2 `NmtField` objects with distinct Python identities; coupling order `compute_coupling_matrix(f2,f3,...)`; same-object handoff forbidden.

DES/NaMaster contract: NSIDE=4096, ell `0..12287`, 39 bands, full BPW `[4,39,4,12288]`, selected `<f8 [39,12288]` with `wins[0,:,0,:]=EE<-EE`; public file-backed NaMaster 2.7 serialized-workspace route; exact `/proc/self/maps` MCM proof and backing size `19,327,352,832` bytes.

S2 authority: selected `8,238,547`; bytes `32,954,188`; record SHA `259295a1f5a23ad9e5c6b46842bcf612b0eb13dc701ab6d54eb15f0d7bb0105f`; unique `4,401,919`; occupancy SHA `9e2bfb92289ca4a3abb11efabf7ac8d59bb7c68eb63a7104c2b247267733b24d`.

S3 authority: selected `4,196,641`; bytes `16,786,564`; record SHA `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec`; unique `2,943,132`; occupancy SHA `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094`.

Common source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; R1 artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`; NaMaster head `24365fa59a38c15732f4f37e8b29265b75c442d5`; patch blob `d534b698f9131688d263eedcef27260386c58641`.

Replicas A/B use disjoint six-stage checkpoints with complete-chain verification before pruning. Candidate PASS requires exact selected SHA equality, `numpy.array_equal`, all finite, ordered `[2,3]` distinct-field semantics, exact file-backed proof, and no historical/cross-replica numerical import.

PASS token: `PASS_EXP073FY_WW_S2_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`. Candidate creates no authority; separate `Exp073FZ` admission required. Exact mismatch is scientific FAIL. No tolerance/allclose/isclose/rounding/smoothing/averaging/manual reconstruction/effective-coordinate/fiducial-P rescue and no downstream scoring.
