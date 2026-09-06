# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-06
**Scope:** DSIR only; RTK/RQIR excluded.

Repository state, immutable recovery notes, validated raw Actions logs/artifacts and durable checkpoints outrank chat wording. Historical outcomes remain immutable. Never upgrade support evidence into science authority.

## Preserved authority and frontier
Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 exact scientific PASS remain preserved. `WW_S0_S0` remains admitted by Exp073EO v0.2 run/job `34005373819 / 101411448176`, artifact `9980754356`, independently verified digest `sha256:0e1a4cff3b761fecc65d8e07df9e56f8109fd221fb4454746caa8c7d0f2fb4be`, token `PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_2`. Exp073EL full-resolution resource readiness remains support PASS `+0/+0`: run `34005467421`, artifact `9980783193`, independently verified digest `sha256:c720233664be2e8a7666db6f95def0a2f13eb674732add6852f0c09e916e5e46`.

Current science target is **WW_S0_S1**. Frozen order remains `Wm_S1 -> Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.

## Exp073EY terminal failure consumed
Corrected Exp073EY run `34006214398`, hosted preflight `101413770925` SUCCESS, self-hosted job `101413789646` FAILURE. Artifact `9982181156`; GitHub digest and independently downloaded ZIP SHA256 both equal `9b600273307c915cba691a998ea33a9443f188a8d4f81f03bc60fb471c0a61c5`.

The raw artifact proves replica A completed exactly these durable stages:
`fresh_sources_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified`.
A source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, workspace FITS SHA `ccadf25f8724acfbd29c16135674e0f845e98d99644be3d6c55526f03dbe241b`. No A full-window/selected/receipt, no B numerical result, no A/B comparison and no terminal scientific token were produced.

First causal exception: `RuntimeError: fail-closed file-backed FITS read candidate count 0` after A workspace construction/FITS verification. Classification is therefore **`INFRASTRUCTURE_SOFTWARE_PATCH_BINDING_FAIL +0/+0`**, not a WW_S0_S1 scientific FAIL.

### Exact cause
The failed EY envelope bound `patches/namaster-v2.7-dsir-filebacked-mcm-v0.1.patch`, blob `f1eb886ca8af2584a9f621f333cd8be3c6cdb967`. It implements file-backed allocation for construction in `src/nmt_master.c` but does not patch the FITS-read allocator in `src/nmt_io.c`; therefore the fail-closed public-read adapter correctly sees zero new `dsir-nmt-mcm-*` files.

The already prospectively qualified Exp073ER patch `patches/namaster-v2.7-dsir-filebacked-mcm-read-v0.2.patch`, blob `d534b698f9131688d263eedcef27260386c58641`, shares the storage-only allocator with `src/nmt_io.c`. Exp073ER run/job `33997539503 / 101390573286`, artifact `9978528214`, independently verified digest `sha256:1e0c3516de041e773eca030d9488f7af7d38455033ae5b97ba1151820eb22267`, proved exact stock↔patched public FITS-read BPW equality and live regular-file mmap semantics. This is support `+0/+0`, not science authority.

## Prospectively frozen repair
Erratum `experiments/073ey_ww_s0_s1_filebacked_full_resolution_ab_science_v0_5_read_patch_repair_erratum.md`, blob `a6fc7a1a3af86f8f02eba8c02294283192642784`.
Repair wrapper `ci/exp073ey_home_filebacked_fullres_v0_2.sh`, blob `a9cabeadc9b091424246adf00e9959dc62145e9b`.
It retains the frozen v0.1 home envelope and original science-driver blobs `1db1eabbdba492c476cc61d3c4d71147aa688384` and `066847006b2ed9d712d2c22d3576a0d8887fa7bf`, changing only the storage patch bound to the already-qualified read-capable v0.2 patch. It still runs the local exact Exp073EM storage qualifier before science.

Hosted fail-closed repair audit: run/job `34010599584 / 101425618749` = SUCCESS. It binds erratum/wrapper/base-driver/read-patch identities and Exp073ER terminal authority.

## Current authoritative process
Workflow `Exp073EY WW_S0_S1 checkpoint resume v0.2`, run **`34010599584`**, head **`4c570bf6b7f3f53547f43e2882149defa125da89`**:
- hosted repair audit `101425618749`: SUCCESS;
- home checkpoint-resume science job **`101425638857`: IN_PROGRESS** at latest reconciliation.

**DSIR-HOME-PC is reserved exclusively for `34010599584 / 101425638857`. Never launch a competing self-hosted DSIR run.**

Checkpoint namespaces are unchanged: A `checkpoints/exp073ey-ww-s0-s1-a-v0-1`; B `checkpoints/exp073ey-ww-s0-s1-b-v0-1`. Last verified durable state is replica A `mcm_fits_verified`; all three A stages must be restored by exact source/contract/manifest/payload SHA verification and must not be recomputed. Replica B has no admitted checkpoint from the failed attempt.

Frozen Exp073EY science remains: ordered distinct `(S0,S1)`; DES NSIDE=4096; ell `0..12287`; 39 bands; distinct spin-2 fields; exact `compute_coupling_matrix(f0,f1,b)`; public `read_from(..., read_unbinned_MCM=True) -> get_bandpower_windows()`; one regular file-backed unbinned MCM exactly `19,327,352,832` bytes visible in `/proc/self/maps`; full BPW `[4,39,4,12288]`; selected `EE<-EE = wins[0,:,0,:]`; canonical `<f8 [39,12288]`; exact A/B SHA256 plus `numpy.array_equal`; finiteness; no tolerance/allclose/rounding/smoothing/averaging/effective-ell/fiducial rescue.

Expected candidate token remains `PASS_EXP073EY_WW_S0_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`. Workflow SUCCESS alone is not science PASS.

## Exp073EZ next admission gate — resume binding prospectively repaired
Base immutable preregistration remains `experiments/073ez_ww_s0_s1_filebacked_checkpoint_provenance_admission_v0_1_prereg.md`, commit `73bfd98efb1a1e2535f644f48dbf5ee5a01dcd88`, blob `346bdbedcb34bdd67a0df88e5444f08071e822b6`.

A governance audit found that v0.1 still bound the candidate execution to the original failed Exp073EY run. Before any terminal resume result was known and without reading partial numerical output, provenance-only erratum `experiments/073ez_ww_s0_s1_filebacked_checkpoint_provenance_admission_v0_2_resume_binding_erratum.md` was frozen: commit `d694c80fd488b60faaea68a37294ee85cff5fe77`, blob `c5125bb9a09f6c02a1d6b48a862902ead9127b61`.

The erratum changes execution/provenance binding only: candidate run/job `34010599584 / 101425638857`, activation/head `4c570bf6b7f3f53547f43e2882149defa125da89`, resume workflow blob `7c0e8718357cfe4448b26c372a0567edf860f572`, repair erratum/wrapper/read-patch identities. It preserves the v0.1 scientific arithmetic, exact acceptance gate, ordered six-stage checkpoint chains and authority token unchanged. Terminal artifact ID/digest/result remain deliberately unknown until terminal.

Hosted static audit run/job `34012838925 / 101431487475` = SUCCESS; raw token `PASS_EXP073EZ_RESUME_BINDING_STATIC_AUDIT_V0_1`. This is governance/support `+0/+0`, not WW authority. Exp073EZ remains `PREREGISTERED_NOT_ACTIVATED`. Only token `PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1` may create `WW_S0_S1` authority.

## Frozen global boundaries
`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid-row `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

## Exact next actions
1. Do not duplicate or disturb Exp073EY resume `34010599584 / 101425638857`.
2. On terminal, download the compact artifact and independently verify ZIP SHA256, restored-vs-new stage provenance, source/contract/driver/patch identities, both six-stage chains, file-backed mmap proof, exact A/B selected equality/finiteness and terminal token.
3. On valid candidate PASS, bind exact terminal run/job/artifact/digest into Exp073EZ under immutable v0.1 plus v0.2 resume-binding erratum and run hosted provenance admission; only EZ PASS admits WW_S0_S1, then advance to WW_S0_S2.
4. On genuine completed exact A/B mismatch, record WW_S0_S1 scientific FAIL and continue without tuning the gate.
5. On infrastructure/resource/provenance/checkpoint failure, diagnose first cause, preserve verified complete stages, repair minimally and resume without recomputing verified expensive work.

Current immutable recovery note: `docs/recovery/RECOVERY_2026-09-06_EXP073EZ_RESUME_BINDING_PREREG_AUDIT.md`.
