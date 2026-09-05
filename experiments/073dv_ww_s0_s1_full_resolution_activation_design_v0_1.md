# Exp073DV — WW_S0_S1 full-resolution activation design v0.1

Prepared prospectively on 2026-09-05 while Exp073DT `WW_S0_S0` remained queued, before any `WW_S0_S1` full-resolution numerical output exists. This file is design/readiness only: it does **not** activate a workflow, score a science gate, or create `WW_S0_S1` authority.

## Entry conditions
Exp073DV may be activated only after repository authority records all of the following:
1. `WW_S0_S0` is terminally classified from Exp073DT raw evidence, not workflow status alone.
2. If Exp073DT is PASS, Exp073EB full six-stage checkpoint-provenance audit is PASS support-only `+0/+0`.
3. Exp073DU distinct-field cross-workspace qualifier is consumed and classified support-only; a qualifier failure must be diagnosed before full-resolution activation.
4. Live Actions reconciliation shows no queued/in-progress competing self-hosted DSIR heavy process.

No result-dependent modification of the frozen `WW_S0_S1` arithmetic is permitted after these entry conditions are observed.

## Frozen science geometry for the future activation
- Task exactly `WW_S0_S1`.
- DES source bins are ordered `(S0,S1)` as parsed by the canonical Article-3 task runner; no lens mask may be read.
- NSIDE=4096; ell axis `0..12287`; the existing 39 frozen band edges are unchanged.
- Construct two distinct spin-2 `NmtField` objects from independently reconstructed authoritative S0 and S1 source count maps. Never replace the ordered cross workspace with either `S0_S0` or `S1_S1` auto workspace.
- Persist stock full WW window with exact shape `[4,39,4,12288]` and select exactly `wins[0,:,0,:] = EE<-EE`.
- Canonical selected payload is contiguous `<f8 [39,12288]`.
- No effective ell/z/k, no fiducial-P shortcut, no tolerance/allclose/rounding/smoothing/averaging rescue.

## Source/provenance requirements
The activation must bind exact source authority, contract fingerprint and component Git blobs prospectively. It must independently validate the R1 artifact and reconstruct both S0 and S1 from their authoritative pixel-record streams using the canonical `source_count_map` path.

For each replica, checkpoint evidence must bind and hash **both** source maps and their identities. A completed S0/S1 map may restore only after exact namespace/source-head/contract/payload SHA/shape/dtype verification. Cross-workspace evidence must record ordered field semantics `(S0,S1)` and workspace FITS SHA.

## Durable A/B checkpoint architecture
Use two independent namespaces under a dedicated Exp073DV durable root. The complete-stage chain must be prospectively frozen before activation and include, at minimum:

`fresh_s0_s1_masks_complete -> fresh_cross_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_ee_complete -> replica_receipt_complete`

Every complete stage gets an atomic manifest with source head, contract fingerprint, replica identity, namespace, payload SHA256, and `historical_ww_numerical_import=false`. Interrupted stages are not resumable as complete. A verified complete expensive workspace must not be recomputed unnecessarily.

The terminal fast-path must not repeat the Exp073DT evidence gap: before treating a replica as finished it must reread and validate the full ordered manifest chain, not only the final receipt/selected payload. Terminal artifact evidence should export enough manifest/receipt data for independent authority review without relying on mutable local state.

## Resource contract
For any home full-resolution activation: exactly one self-hosted DSIR heavy process; one continuous nonblocking flock over the whole science body; exactly 8 outer compute workers where the implementation exposes independent complete-band/task units; nested OpenBLAS/MKL/NumExpr/BLIS/other numerical-library threads pinned to 1; durable checkpoint after each complete unit/stage; exact canonical reassembly and SHA/array verification. No arithmetic change for performance.

If the cross-workspace construction cannot safely use the repository's established 8-core/durable architecture, activation is BLOCKED until a prospective implementation preserves identical scientific arithmetic with fail-closed resume semantics.

## Future scientific terminal rule
The future preregistration/activation must freeze a unique token before full-resolution output exists. Scientific PASS is allowed only if two independent fresh/resumed replicas produce exact identical canonical selected EE payloads (`SHA256_equal=true` and `numpy.array_equal=true`) with complete source/workspace/checkpoint provenance and no tolerance rescue.

Exact A/B inequality is a scientific repeatability FAIL. Runner loss, timeout, dependency/runtime error, malformed artifact, missing/corrupt checkpoint, source/contract mismatch or provenance incompleteness is infrastructure/BLOCKED `+0/+0` and must not be converted into a scientific result.

## Status
`PREPARED_NOT_ACTIVATED`, `science_gate_scored=false`, `ww_s0_s1_authority_created=false`.
