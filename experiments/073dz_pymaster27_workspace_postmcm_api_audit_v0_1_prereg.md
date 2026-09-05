# Exp073DZ — PyMaster 2.7 workspace post-MCM API audit v0.1

Scope: DSIR only. Support/diagnostic only `+0/+0`; no WW authority may be created.

Motivation: Exp073DY run 33970593677 failed before any numerical comparison because the diagnostic referenced nonexistent `NmtWorkspace.bpws`. This is an infrastructure/software failure, not a scientific result.

Frozen diagnostic: on GitHub-hosted Ubuntu with PyMaster 2.7, construct a deterministic spin-2 cross workspace at NSIDE=16, serialize and reload it, and record only the available public/high-level and low-level `wsp` attributes needed to reconstruct the post-MCM path. Record shapes/types for `get_bandpower_windows()`, `get_coupling_matrix()`, `wsp.bin`, and candidate low-level fields among `mcm_binned`, `mcm`, `norm_type`, `wawb`, `beam1`, `beam2`, `ncls`, `lmax`. Also record whether the original deterministic `NmtBin` exposes `_bin_mcm`.

No numerical acceptance criterion is scored. No tolerance, rounding, smoothing, averaging, permutation, transpose rescue, or result-dependent branch is allowed. The only terminal token is `COMPLETE_EXP073DZ_PYMASTER27_WORKSPACE_POSTMCM_API_AUDIT_V0_1`; any runtime error is infrastructure `+0/+0`.
