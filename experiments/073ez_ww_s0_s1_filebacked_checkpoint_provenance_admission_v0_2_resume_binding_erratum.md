# Exp073EZ — WW_S0_S1 provenance admission v0.2 resume-binding erratum

Date: 2026-09-06. Scope: DSIR only. This erratum is created prospectively while the authoritative Exp073EY checkpoint-resume science job `34010599584 / 101425638857` is still `IN_PROGRESS`. No partial Exp073EY numerical output was inspected or used.

## Purpose

The immutable Exp073EZ v0.1 preregistration remains historical authority for the scientific and checkpoint/provenance acceptance rules, but its upstream execution binding names the original Exp073EY run `34006214398` / activation head `0476ce61a84a97392abb80afadad188a588bbe1f`. That run has since terminated with `INFRASTRUCTURE_SOFTWARE_PATCH_BINDING_FAIL +0/+0` before any full-window A/B scientific result. A prospectively audited checkpoint-preserving repair/resume is now the authoritative candidate-producing process. Therefore v0.1 cannot literally admit the resume candidate unless the execution binding is corrected before the result is known.

This erratum changes provenance binding only. It does **not** change any scientific arithmetic, geometry, field order, acceptance criterion, exactness rule, checkpoint stage semantics, resource requirement, or authority-writing token.

## Frozen immutable base retained

Base admission preregistration remains:
- `experiments/073ez_ww_s0_s1_filebacked_checkpoint_provenance_admission_v0_1_prereg.md`
- blob `346bdbedcb34bdd67a0df88e5444f08071e822b6`.

All v0.1 scientific semantics remain unchanged, including ordered distinct `(S0,S1)`, DES NSIDE=4096, ell `0..12287`, 39 bands, regular-file-backed unbinned MCM exactly `19,327,352,832` bytes, full BPW `[4,39,4,12288]`, selected `EE<-EE = wins[0,:,0,:]`, canonical `<f8 [39,12288]`, exact SHA256 + `numpy.array_equal`, finiteness, six-stage A/B checkpoint chains, no tolerance/allclose/rounding/smoothing/averaging/effective-ell/fiducial rescue, and no historical numerical import.

The authority-writing token remains exactly:
`PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.

## Superseded execution binding only

For the candidate artifact to be admitted, replace only the v0.1 original-run execution binding with the following current authoritative repair/resume binding:

- authoritative workflow: `.github/workflows/exp073ey-ww-s0-s1-filebacked-ab-resume-v0-2.yml`;
- workflow blob: `7c0e8718357cfe4448b26c372a0567edf860f572`;
- resume run: `34010599584`;
- hosted repair-audit job: `101425618749`, required terminal `SUCCESS`;
- self-hosted candidate-producing job: `101425638857`;
- activation/head SHA: `4c570bf6b7f3f53547f43e2882149defa125da89`;
- repair erratum blob: `a6fc7a1a3af86f8f02eba8c02294283192642784`;
- repair wrapper blob: `a9cabeadc9b091424246adf00e9959dc62145e9b`;
- qualified FITS-read storage patch blob: `d534b698f9131688d263eedcef27260386c58641`;
- original scientific driver blobs remain `1db1eabbdba492c476cc61d3c4d71147aa688384` and `066847006b2ed9d712d2c22d3576a0d8887fa7bf`;
- frozen source authority remains `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- frozen contract fingerprint remains `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- checkpoint namespaces remain `checkpoints/exp073ey-ww-s0-s1-a-v0-1` and `checkpoints/exp073ey-ww-s0-s1-b-v0-1`.

The original failed run `34006214398` and its artifact remain immutable historical infrastructure evidence. They MUST NOT be rewritten as a scientific result and MUST NOT be used as the terminal candidate artifact for admission.

## Resume provenance requirements

The eventual terminal resume artifact must additionally prove, fail-closed:

1. Replica A stages `fresh_sources_complete`, `fresh_workspace_mcm_complete`, and `mcm_fits_verified` were restored from the previously verified durable checkpoint chain by exact manifest/source/contract/payload SHA checks and were not recomputed unnecessarily.
2. Any later A stages and all B stages identify whether they were restored or newly computed and preserve the exact six-stage ordering required by v0.1.
3. The repair changes storage/FITS-read binding only; the frozen scientific driver identities above remain exact.
4. The read-capable patch identity is exactly `d534b698f9131688d263eedcef27260386c58641` and the live regular-file mmap proof is present for the required `19,327,352,832`-byte unbinned MCM.
5. The terminal candidate token remains exactly `PASS_EXP073EY_WW_S0_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`.
6. Workflow/job success alone is never sufficient.

## Deliberately unknown until terminal

This erratum deliberately does **not** freeze or guess the terminal artifact ID, GitHub artifact digest, independently recomputed ZIP SHA256, terminal selected-array SHA256 values, or terminal classification. These may be bound into the actual Exp073EZ admission implementation only after `34010599584 / 101425638857` is terminal and the artifact is independently consumed.

If the resume ends with a fully qualified exact A/B mismatch, that remains a genuine `WW_S0_S1` scientific FAIL under v0.1 and this erratum cannot rescue it. If it ends with infrastructure/resource/provenance/checkpoint failure, classification remains `+0/+0` and no WW_S0_S1 authority is created.

Status: `PREREGISTERED_NOT_ACTIVATED`; `ww_s0_s1_authority_created=false`.
