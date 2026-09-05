# Exp073DO — WW_S0_S0 exact adapter static admission v0.1

Frozen 2026-09-05 after raw Exp073DN support PASS and before any WW_S0_S0 numerical production.

Scope is implementation/readiness `+0/+0` only. No WW authority may be created.

Parent: Exp073DN run/job `33938100671 / 101229887636`, artifact `9960842558`, digest `sha256:955cbe2f58b1809fec34815d33b105edac8f02777f99e6d4e36f57b29f64a259`, raw token `PASS_EXP073DN_REQUIRE_WW_SPECIFIC_CHECKPOINT_ADAPTER_V0_1`.

Implement a WW-specific exact adapter derived only from the already-audited canonical FITS->mmap->downstream architecture, with these frozen differences from Wm:

- require `ncls=4`, never 2;
- full output exactly `[4,nb,4,nl]`;
- select canonical `wins[0,:,0,:]` as `EE<-EE` into `selected_ee.bin`;
- receipt names `ww_s0_s0_authority_created=false`, `selected_ee_sha256`, `selected_ee_shape`;
- durable semantic label `selected_ee_complete`, never TE;
- retain source-head, contract-fingerprint, checkpoint namespace and component-blob binding;
- retain mmap proof, exact byte-size checks, no `get_coupling_matrix()` materialization, no tolerance rescue;
- downstream executable must be generic in `ncls` and its 8-worker build must runtime-prove exactly `DSIR_OMP_TEAM=8`; scalar accumulation order may not change.

Static PASS token: `PASS_EXP073DO_WW_EXACT_ADAPTER_STATIC_ADMISSION_V0_1` only if machine inspection proves the new adapter contains no Wm/lens/S3/TE production semantics, requires ncls=4, selects EE exactly, and the reused downstream C source accepts generic ncls through at least 4 while preserving deterministic per-scalar accumulation order.

A PASS authorizes only a later hosted small-NSIDE exact-equivalence audit against stock PyMaster WW bandpower windows, followed by a separate durable WW A/B driver audit. It does not authorize home scientific execution.

Any source mismatch is `BLOCKED_EXP073DO_WW_EXACT_ADAPTER_STATIC_ADMISSION`, still `+0/+0`.