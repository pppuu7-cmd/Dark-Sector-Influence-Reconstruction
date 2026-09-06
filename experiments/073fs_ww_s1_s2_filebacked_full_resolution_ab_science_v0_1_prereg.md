# Exp073FS — WW_S1_S2 file-backed full-resolution A/B science v0.1

Date frozen: 2026-09-06. Scope: DSIR Article-3 angular authority.

## Entry condition

This heavy target may start only after `WW_S1_S1` is independently admitted with exact token `PASS_EXP073FR_WW_S1_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`. Any missing/failed predecessor admission blocks launch.

## Frozen target and semantics

- ordered target: `WW_S1_S2`
- authoritative source indices: `[1,2]`
- source pair: `S1->S2`; reversed `S2->S1` is forbidden
- reconstruct S1 exactly once and S2 exactly once per replica
- construct exactly two spin-2 `NmtField` objects from the independently reconstructed S1 and S2 maps
- the two field objects MUST have distinct Python identities; same-object handoff is forbidden
- coupling order: `compute_coupling_matrix(f1,f2,...)`
- DES NSIDE=4096; ell `0..12287`; 39 bands
- public file-backed NaMaster 2.7 route: serialized workspace `read_from(..., read_unbinned_MCM=True)` then public `get_bandpower_windows()`
- exact full BPW geometry `[4,39,4,12288]`
- canonical selected array `<f8 [39,12288]`, `wins[0,:,0,:] = EE<-EE`
- exact file-backed MCM `/proc/self/maps` proof, backing bytes exactly `19,327,352,832`

## Frozen source authorities

S1:
- selected records `7,851,711`
- record bytes `31,406,844`
- record SHA-256 `752f585125e413c7bd40cc5174cf7ef98e95f970022a351c5d91206f371d2241`
- unique pixels `4,339,193`
- occupancy SHA-256 `fed1ffdf2ef7a7ae88e42615bd08e207e039239c44fa20b7994258f147a739f1`

S2:
- selected records `8,238,547`
- record bytes `32,954,188`
- record SHA-256 `259295a1f5a23ad9e5c6b46842bcf612b0eb13dc701ab6d54eb15f0d7bb0105f`
- unique pixels `4,401,919`
- occupancy SHA-256 `9e2bfb92289ca4a3abb11efabf7ac8d59bb7c68eb63a7104c2b247267733b24d`

Frozen common authority:
- source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`
- R1 artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`
- NaMaster head `24365fa59a38c15732f4f37e8b29265b75c442d5`
- file-backed patch blob `d534b698f9131688d263eedcef27260386c58641`

## Durable A/B protocol

Replicas A and B use disjoint checkpoint namespaces. Each replica must preserve six completed-stage manifests: `fresh_sources_complete`, `fresh_workspace_mcm_complete`, `mcm_fits_verified`, `full_window_complete`, `selected_ee_complete`, `replica_receipt_complete`. All still-present payload hashes are revalidated before pruning; large source/workspace/full-window payloads may be pruned only after the complete chain is bound into a prune receipt. Terminal A/B comparison consumes only prospectively bound terminal/prune evidence and selected EE arrays; it may not restore a completed replica.

## Scientific scoring

Candidate PASS requires simultaneously:
- A and B complete-chain verification before prune;
- exact A/B selected SHA-256 equality;
- `numpy.array_equal(A,B)`;
- all finite;
- ordered `[1,2]`, distinct-field semantics on both replicas;
- public file-backed route and exact MCM backing proof;
- no historical WW numerical import and no other-replica numerical reads.

PASS token: `PASS_EXP073FS_WW_S1_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`.

A candidate PASS creates **no scientific authority**. A separate hosted provenance-admission job must pass before `WW_S1_S2` is admitted. Exact numerical mismatch is a scientific FAIL. Infrastructure/resource failures are classified separately and may resume only from already valid complete checkpoints without changing frozen arithmetic.

Forbidden: `allclose`, `isclose`, tolerance rescue, rounding, smoothing, averaging, manual BPW reconstruction, effective-coordinate/fiducial-P shortcuts, reversed source order, same-field reuse, and downstream 14-window/radial/covariance/relation scoring.
