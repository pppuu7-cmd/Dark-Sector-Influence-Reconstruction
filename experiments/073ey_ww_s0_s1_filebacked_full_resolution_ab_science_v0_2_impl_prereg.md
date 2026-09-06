# Exp073EY v0.2 implementation preregistration — public-route file-backed proof

Date frozen: 2026-09-06, before any Exp073EY numerical execution. DSIR only.

The scientific gate remains exactly the already frozen `experiments/073ey_ww_s0_s1_filebacked_full_resolution_ab_science_v0_1_prereg.md` (blob `a2970a4332d415817b011c6ce73049f0083ada93`). No domain, source order, banding, geometry, exact-equality rule, checkpoint rule, or PASS/FAIL criterion changes.

The first pre-launch implementation draft was corrected before activation because it initially referenced the historical saved-FITS reconstruction adapter. Commit `9a8d30abe7f6a8098eb3701d797b4221b70c7ea6`, blob `1db1eabbdba492c476cc61d3c4d71147aa688384`, removed that adapter and uses only `NmtWorkspace.read_from(..., read_unbinned_MCM=True)` followed by public `get_bandpower_windows()` and exact selection `wins[0,:,0,:]`.

A second pre-launch static design check found that this corrected draft attempted to prove file-backed ownership by reading `w2.wsp.mcm`. That member is not a guaranteed Python-visible PyMaster 2.7 surface and therefore must not be a production admission dependency.

The v0.2 implementation repair is limited to replacing that proof mechanism. After `read_from(..., read_unbinned_MCM=True)`, the process must identify the unique `dsir-nmt-mcm-*` regular backing file in the prospectively supplied `DSIR_NMT_MMAP_DIR`, require exact size `19327352832` bytes, require its resolved path to occur in `/proc/self/maps`, and only then call public `get_bandpower_windows()`. No hidden `wsp.mcm` access is allowed. The exact public full shape `[4,39,4,12288]`, selected `EE<-EE [39,12288]`, canonical `<f8`, finiteness, SHA, `numpy.array_equal`, ordered `(S0,S1)`, six-stage checkpoint architecture, and no-rescue policy remain unchanged.

The v0.2 executable may import the frozen v0.1 implementation blob `1db1eabbdba492c476cc61d3c4d71147aa688384`, override only `public_bpw_from_serialized_workspace`, and invoke its unchanged `main()`. This is an implementation/proof repair before first data, not post-hoc scientific tuning.

Before any self-hosted Exp073EY launch, a hosted static audit must bind both prereg blobs and both driver blobs and fail closed unless the effective route contains `read_unbinned_MCM=True`, exact backing-file size `19327352832`, `/proc/self/maps`, `get_bandpower_windows()`, exact `[0,:,0,:]`, distinct ordered `f0,f1`, exact-only A/B comparison, checkpoint namespaces, and no historical adapter/tolerance rescue.
