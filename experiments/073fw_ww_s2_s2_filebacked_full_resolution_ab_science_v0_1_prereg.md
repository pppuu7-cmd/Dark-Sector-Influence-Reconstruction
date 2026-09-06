# Exp073FW — WW_S2_S2 file-backed full-resolution A/B science v0.1

Date frozen: 2026-09-06. Scope: DSIR Article-3 angular authority.

## Entry condition

This heavy target may start only after `WW_S1_S3` is independently admitted with exact token `PASS_EXP073FV_WW_S1_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`. Any missing/failed predecessor admission blocks launch.

## Frozen target and semantics

- ordered target: `WW_S2_S2`
- authoritative source indices: `[2,2]`
- source pair: `S2->S2`
- reconstruct authoritative S2 exactly once per replica
- construct exactly one spin-2 `NmtField` per replica
- pass the same Python field object to both sides of `compute_coupling_matrix(f2,f2,...)`; equal-but-distinct second field is forbidden
- DES NSIDE=4096; ell `0..12287`; 39 bands
- public file-backed NaMaster 2.7 route: serialized workspace `read_from(..., read_unbinned_MCM=True)` then public `get_bandpower_windows()`
- full BPW `[4,39,4,12288]`; canonical selected `<f8 [39,12288]`, `wins[0,:,0,:] = EE<-EE`
- exact MCM backing proof in `/proc/self/maps`, backing bytes exactly `19,327,352,832`

## Frozen S2 authority

- selected records `8,238,547`
- record bytes `32,954,188`
- record SHA-256 `259295a1f5a23ad9e5c6b46842bcf612b0eb13dc701ab6d54eb15f0d7bb0105f`
- unique pixels `4,401,919`
- occupancy SHA-256 `9e2bfb92289ca4a3abb11efabf7ac8d59bb7c68eb63a7104c2b247267733b24d`

Frozen common authority: source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; R1 artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`; NaMaster head `24365fa59a38c15732f4f37e8b29265b75c442d5`; patch blob `d534b698f9131688d263eedcef27260386c58641`.

## Durable A/B and scoring

Replicas A/B use disjoint six-stage checkpoint namespaces. Complete-chain payload hashes are revalidated before pruning. Terminal comparison consumes only bound terminal/prune evidence and selected EE arrays and may not restore a completed replica.

Candidate PASS requires exact selected SHA-256 equality, `numpy.array_equal`, all finite, `[2,2]` same-object semantics on both replicas, public file-backed route, exact MCM backing proof, no historical WW numerical import and no other-replica numerical read.

PASS token: `PASS_EXP073FW_WW_S2_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`.

Candidate PASS creates no authority. A separate hosted provenance admission `Exp073FX` is mandatory. Exact mismatch is a scientific FAIL. Infrastructure/resource failures do not change frozen arithmetic and may resume only from valid complete checkpoints.

Forbidden: `allclose`, `isclose`, tolerance rescue, rounding, smoothing, averaging, manual BPW reconstruction, effective-coordinate/fiducial-P shortcuts, distinct second field for this auto-window, and downstream 14-window/radial/covariance/relation scoring.
