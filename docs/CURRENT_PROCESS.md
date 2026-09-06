# DSIR current-process ledger

Updated: 2026-09-06
Scope: DSIR only; RTK/RQIR excluded.

## Preserved scientific authority
Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 exact scientific PASS remain preserved. `WW_S0_S0` remains admitted by Exp073EO v0.2 run/job `34005373819 / 101411448176`, artifact `9980754356`, digest `sha256:0e1a4cff3b761fecc65d8e07df9e56f8109fd221fb4454746caa8c7d0f2fb4be`, token `PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_2`. Exp073EL resource readiness remains PASS +0/+0 with artifact `9980783193`, digest `sha256:c720233664be2e8a7666db6f95def0a2f13eb674732add6852f0c09e916e5e46`.

## Consumed Exp073EY failure
Original corrected EY run/job `34006214398 / 101413789646` is terminal FAILURE, classified `INFRASTRUCTURE_SOFTWARE_PATCH_BINDING_FAIL +0/+0`, not scientific FAIL. Artifact `9982181156` has GitHub and independently downloaded ZIP SHA256 `9b600273307c915cba691a998ea33a9443f188a8d4f81f03bc60fb471c0a61c5`.

First causal exception: `fail-closed file-backed FITS read candidate count 0`. Replica A valid durable stages preserved from raw artifact: `fresh_sources_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified`; workspace FITS SHA `ccadf25f8724acfbd29c16135674e0f845e98d99644be3d6c55526f03dbe241b`. No full-window, selected-EE, replica receipt, B science result, A/B result or terminal science token was produced.

Causal defect: EY bound construction-only patch `patches/namaster-v2.7-dsir-filebacked-mcm-v0.1.patch` blob `f1eb886ca8af2584a9f621f333cd8be3c6cdb967`, which does not patch `src/nmt_io.c`. The already qualified Exp073ER read-capable storage patch is `patches/namaster-v2.7-dsir-filebacked-mcm-read-v0.2.patch`, blob `d534b698f9131688d263eedcef27260386c58641`; Exp073ER `33997539503 / 101390573286`, artifact `9978528214`, digest `sha256:1e0c3516de041e773eca030d9488f7af7d38455033ae5b97ba1151820eb22267` proved exact public FITS-read BPW semantics.

## Authoritative current process — Exp073EY checkpoint resume
Workflow: `Exp073EY WW_S0_S1 checkpoint resume v0.2`.

- run `34010599584`;
- hosted repair-audit job `101425618749`: SUCCESS;
- self-hosted home resume job `101425638857`: IN_PROGRESS;
- activation/head SHA `4c570bf6b7f3f53547f43e2882149defa125da89`;
- repair erratum blob `a6fc7a1a3af86f8f02eba8c02294283192642784`;
- repair wrapper blob `a9cabeadc9b091424246adf00e9959dc62145e9b`;
- read-capable patch blob `d534b698f9131688d263eedcef27260386c58641`;
- original scientific driver blobs remain `1db1eabbdba492c476cc61d3c4d71147aa688384` and `066847006b2ed9d712d2c22d3576a0d8887fa7bf`;
- frozen source head remains `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint remains `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- checkpoint namespaces remain `checkpoints/exp073ey-ww-s0-s1-a-v0-1` and `checkpoints/exp073ey-ww-s0-s1-b-v0-1`.

Frozen science remains ordered distinct `(S0,S1)`, NSIDE=4096, ell `0..12287`, 39 bands, public serialized-workspace `read_from(..., read_unbinned_MCM=True) -> get_bandpower_windows()`, exact regular-file MCM size `19,327,352,832` bytes, selected `EE<-EE = wins[0,:,0,:]`, canonical `<f8 [39,12288]`, exact SHA256 plus `numpy.array_equal`, finiteness, no tolerance/rounding/smoothing/averaging rescue.

**Runner ownership:** DSIR-HOME-PC is reserved exclusively for `34010599584 / 101425638857`. No competing self-hosted DSIR run is permitted.

**Last verified durable checkpoint:** replica A `mcm_fits_verified`; its earlier complete stages must be restored by exact manifest/source/contract/payload SHA checks rather than recomputed. Replica B has no admitted science checkpoint from the failed run.

## Prospectively repaired Exp073EZ admission binding
The immutable Exp073EZ v0.1 preregistration blob `346bdbedcb34bdd67a0df88e5444f08071e822b6` retained the original failed EY execution binding and therefore could not literally admit a valid resume candidate. Before any terminal resume result was known, provenance-only erratum `experiments/073ez_ww_s0_s1_filebacked_checkpoint_provenance_admission_v0_2_resume_binding_erratum.md` was created: commit `d694c80fd488b60faaea68a37294ee85cff5fe77`, blob `c5125bb9a09f6c02a1d6b48a862902ead9127b61`.

It changes execution/provenance binding only and freezes current candidate-producing identities `34010599584 / 101425638857`, head `4c570bf6b7f3f53547f43e2882149defa125da89`, resume workflow blob `7c0e8718357cfe4448b26c372a0567edf860f572`, repair erratum/wrapper/read-patch blobs, while preserving the v0.1 scientific and six-stage checkpoint contract unchanged. Terminal artifact ID/digest/result remain deliberately unbound until terminal.

Hosted static audit run/job `34012838925 / 101431487475` = SUCCESS with raw token `PASS_EXP073EZ_RESUME_BINDING_STATIC_AUDIT_V0_1`. This is support/governance `+0/+0`, not scientific authority.

**On terminal:** consume raw Exp073EY resume artifact and independently verify ZIP SHA256, restored-vs-new stage provenance, exact patch/driver/source/contract identities, public file-backed mmap proof, both six-stage chains, exact A/B selected equality/finiteness and terminal token. Candidate PASS must then instantiate Exp073EZ using v0.1 plus the v0.2 resume-binding erratum. Exact completed mismatch is scientific FAIL; infrastructure/resource/provenance failure remains checkpoint-preserving `+0/+0`. Only `PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1` may create `WW_S0_S1` authority.
