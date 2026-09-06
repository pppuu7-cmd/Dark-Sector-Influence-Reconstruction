# Exp073EY v0.5 — FITS-read storage-patch repair erratum

Date: 2026-09-06
Scope: DSIR only.
Accounting: infrastructure/software repair only; +0/+0 until the frozen Exp073EY science gate itself produces a valid terminal result.

## Frozen scientific identity
This erratum does not change Exp073EY v0.1 science: ordered distinct `(S0,S1)`, NSIDE=4096, ell=0..12287, 39 bands, exact `compute_coupling_matrix(f0,f1,b)`, public serialized-workspace `read_from(..., read_unbinned_MCM=True) -> get_bandpower_windows()`, selected `wins[0,:,0,:] = EE<-EE`, canonical `<f8 [39,12288]`, exact SHA256 plus `numpy.array_equal`, finiteness, and no tolerance/rounding/smoothing/averaging rescue.

Frozen source head remains `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract fingerprint remains `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`.

## Terminal failure consumed
Exp073EY run/job `34006214398 / 101413789646` terminated FAILURE after replica A completed and durably recorded:
`fresh_sources_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified`.
The independently downloaded terminal evidence ZIP for artifact `9982181156` has SHA256 `9b600273307c915cba691a998ea33a9443f188a8d4f81f03bc60fb471c0a61c5`, equal to the GitHub artifact digest.

The first causal exception was `RuntimeError: fail-closed file-backed FITS read candidate count 0` in the public serialized-workspace adapter, after the A workspace MCM and FITS SHA were already complete. No `full_window_complete`, `selected_ee_complete`, replica receipt, B science output, A/B comparison, or scientific terminal token existed. Therefore this is `INFRASTRUCTURE_SOFTWARE_PATCH_BINDING_FAIL +0/+0`, not a WW_S0_S1 scientific FAIL.

## Exact causal defect
The failed EY envelope bound `patches/namaster-v2.7-dsir-filebacked-mcm-v0.1.patch` (blob `f1eb886ca8af2584a9f621f333cd8be3c6cdb967`). That patch changes file-backed allocation in `src/nmt_master.c` for construction, but does not patch `src/nmt_io.c`; therefore `read_from(..., read_unbinned_MCM=True)` does not create a `dsir-nmt-mcm-*` backing file and the adapter correctly fails closed with zero candidates.

The already prospectively qualified Exp073ER path used `patches/namaster-v2.7-dsir-filebacked-mcm-read-v0.2.patch` (blob `d534b698f9131688d263eedcef27260386c58641`). That patch shares the same storage-only allocator between construction and FITS read by patching `src/nmt_io.c`. Exp073ER run/job `33997539503 / 101390573286`, artifact `9978528214`, independently verified digest `sha256:1e0c3516de041e773eca030d9488f7af7d38455033ae5b97ba1151820eb22267`, proved exact stock↔patched public BPW equality and live regular-file mmap semantics for the read path.

## Prospective repair
The only permitted repair is to bind the EY home envelope to the already qualified read-capable v0.2 storage patch. The v0.1 scientific drivers and all frozen scientific identities remain unchanged. Before any resumed science, a hosted fail-closed audit must verify the exact erratum, wrapper, base envelope, driver and read-patch blobs and the terminal Exp073ER authority. The home envelope must still run the local exact Exp073EM storage activation qualifier before science.

Replica A's three verified durable stages are preserved and must be restored by exact source-head/contract/manifest/payload SHA checks; they must not be recomputed. No later stage is admitted from the failed attempt. Replica B has no admitted science checkpoint from that attempt.

Any mismatch in restored checkpoint SHA/identity, read-patch identity, Exp073ER authority, local storage qualifier, mmap proof, public BPW geometry/finiteness or exact A/B comparison fails closed. Scientific thresholds and arithmetic are unchanged.