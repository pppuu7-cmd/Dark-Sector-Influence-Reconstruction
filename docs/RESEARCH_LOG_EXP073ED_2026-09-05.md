# DSIR research log — Exp073ED — 2026-09-05

Exp073DZ terminal evidence was consumed before activation. Artifact `9971589033` independently matched GitHub SHA256 `71a45e8eb21b4a17f7695b8d9cc6c7fe4081513d0d1251ff62494f5ef6352c37` and classified exactly `DIAGNOSTIC_COMPLETE +0/+0`. Observed PyMaster 2.7 reload-state API: public bandpower windows shape `[4,8,4,48]`, coupling matrix `[192,192]`; `NmtWorkspace.bpws` absent; `wsp.bin`, `wsp.ncls`, `wsp.lmax`, `wsp.lmax_fields`, `wsp.norm_type` present; Python-visible `mcm`/`mcm_binned` absent; original `NmtBin._bin_mcm` absent.

Exp073ED is prospectively frozen before result inspection as hosted support-only `+0/+0`. It directly compares the authoritative low-level `pymaster.nmtlib.get_bandpower_windows` buffer, transformed only by the source-defined reshape/transpose, against `NmtWorkspace.get_bandpower_windows()` using exact canonical SHA256 and `numpy.array_equal`. No tolerance/rescue, no production-adapter modification and no WW authority are permitted.

The sole self-hosted heavy authority remains Exp073DT attempt 4 run/job `33940588308 / 101288014666`; it remains reserved and is not duplicated by Exp073ED.