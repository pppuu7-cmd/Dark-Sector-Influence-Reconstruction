# DSIR immutable recovery — Exp073EY patch-binding infrastructure failure and checkpoint-preserving resume

Date: 2026-09-06
Scope: DSIR only; RTK/RQIR excluded.

## Terminal EY result consumed
Run/job `34006214398 / 101413789646` is terminal FAILURE. Evidence artifact `9982181156`; GitHub digest and independently downloaded ZIP SHA256 both equal `9b600273307c915cba691a998ea33a9443f188a8d4f81f03bc60fb471c0a61c5`.

Raw artifact contains replica A complete manifests for `fresh_sources_complete`, `fresh_workspace_mcm_complete`, and `mcm_fits_verified`. Frozen source head is `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract fingerprint is `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; A workspace FITS SHA is `ccadf25f8724acfbd29c16135674e0f845e98d99644be3d6c55526f03dbe241b`. No later A stage, B numerical result, A/B comparison, or terminal science token exists.

First causal traceback is `RuntimeError: fail-closed file-backed FITS read candidate count 0` in `public_bpw_from_serialized_workspace` after A MCM construction and FITS verification. Therefore classification is `INFRASTRUCTURE_SOFTWARE_PATCH_BINDING_FAIL +0/+0`; it is not a `WW_S0_S1` scientific FAIL.

## Cause
The failed EY envelope bound construction-only storage patch `patches/namaster-v2.7-dsir-filebacked-mcm-v0.1.patch`, blob `f1eb886ca8af2584a9f621f333cd8be3c6cdb967`. That patch alters unbinned-MCM allocation in `src/nmt_master.c` but not the FITS read path in `src/nmt_io.c`, so `read_from(..., read_unbinned_MCM=True)` produces no `dsir-nmt-mcm-*` candidate and the fail-closed adapter rejects the run.

The already prospectively qualified Exp073ER read-capable patch `patches/namaster-v2.7-dsir-filebacked-mcm-read-v0.2.patch`, blob `d534b698f9131688d263eedcef27260386c58641`, adds the same storage-only allocator to `src/nmt_io.c`. Exp073ER run/job `33997539503 / 101390573286`, artifact `9978528214`, digest `sha256:1e0c3516de041e773eca030d9488f7af7d38455033ae5b97ba1151820eb22267`, already established exact stock↔patched public FITS-read BPW equality and live regular-file mmap semantics.

## Prospective repair
Repair erratum: `experiments/073ey_ww_s0_s1_filebacked_full_resolution_ab_science_v0_5_read_patch_repair_erratum.md`, blob `a6fc7a1a3af86f8f02eba8c02294283192642784`.
Repair wrapper: `ci/exp073ey_home_filebacked_fullres_v0_2.sh`, blob `a9cabeadc9b091424246adf00e9959dc62145e9b`.
The wrapper retains the frozen v0.1 home envelope and changes only the bound storage-patch path to the qualified read-capable v0.2 patch. It keeps the original scientific driver blobs `1db1eabbdba492c476cc61d3c4d71147aa688384` and `066847006b2ed9d712d2c22d3576a0d8887fa7bf` and still executes the local exact Exp073EM storage qualifier before resumed science.

Hosted repair audit is PASS: run `34010599584`, job `101425618749`. It binds erratum/wrapper/base-driver/read-patch blobs and the terminal Exp073ER support authority.

## Current authoritative process
Same run `34010599584`, self-hosted job `101425638857` is IN_PROGRESS at reconciliation, head `4c570bf6b7f3f53547f43e2882149defa125da89`. DSIR-HOME-PC is exclusively reserved by this job.

Checkpoint namespaces remain unchanged:
- A `checkpoints/exp073ey-ww-s0-s1-a-v0-1`;
- B `checkpoints/exp073ey-ww-s0-s1-b-v0-1`.

Replica A must restore the verified first three stages exactly and must not recompute them. Replica B has no admitted stage from the failed attempt. Frozen science remains ordered `(S0,S1)`, NSIDE=4096, ell 0..12287, 39 bands, `EE<-EE`, canonical `<f8 [39,12288]`, exact SHA/array equality, finiteness and no tolerance rescue.

## Next action
On terminal resume, independently hash the new artifact and validate restored/new stage provenance, patch/source/contract identities, 19,327,352,832-byte file-backed mmap proof, both complete six-stage chains and exact A/B result. A valid candidate PASS still requires the already preregistered Exp073EZ provenance-admission gate before `WW_S0_S1` authority can be created.