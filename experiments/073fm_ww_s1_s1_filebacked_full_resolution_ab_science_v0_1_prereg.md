# Exp073FM — WW_S1_S1 file-backed full-resolution A/B science v0.1 preregistration

Date: 2026-09-06. Scope: **DSIR only**.

Purpose: next heavy Article-3 angular manifest task after WW_S0_S3. Target `WW_S1_S1` only.

Frozen semantic boundary inherited from Exp073FH/FJ/FK:

- authoritative R1 source index `[1]` / source bin `S1`;
- reconstruct authoritative S1 source count map exactly once per replica;
- construct exactly one spin-2 `NmtField` from that S1 source per replica;
- pass the **same field object** on both sides of the WW workspace computation (`fb=fa` semantics);
- equal-but-distinct field objects are forbidden;
- auto-pair only: `[1,1]`; never substitute any cross-pair;
- extract `wins[0,:,0,:] = EE<-EE` from full BPW `[4,39,4,12288]`;
- canonical selected output `<f8 [39,12288]`;
- DES NSIDE=4096, ell `0..12287`, 39 bands;
- file-backed public NaMaster 2.7 route and the previously frozen patch lineage;
- exact A/B SHA plus `numpy.array_equal`; no tolerance/allclose, rounding, smoothing, averaging, manual reconstruction, effective-coordinate or fiducial rescue.

Frozen S1 R1 source authority:

- selected rows: `7851711`
- record bytes: `31406844`
- record SHA256: `752f585125e413c7bd40cc5174cf7ef98e95f970022a351c5d91206f371d2241`
- unique pixels: `4339193`
- occupancy SHA256: `fed1ffdf2ef7a7ae88e42615bd08e207e039239c44fa20b7994258f147a739f1`

The heavy implementation must preserve durable per-replica checkpoint manifests and fully verify each completed replica before pruning large intermediates, following the hardened Exp073FG pattern but transformed to S1_S1 same-field semantics.

Candidate PASS token, if all frozen requirements are met:

`PASS_EXP073FM_WW_S1_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`

Candidate PASS alone creates no authority; a separate provenance-admission gate is mandatory.

No downstream radial/covariance/nuisance/relation/null/G8 scoring is authorized by this experiment.
