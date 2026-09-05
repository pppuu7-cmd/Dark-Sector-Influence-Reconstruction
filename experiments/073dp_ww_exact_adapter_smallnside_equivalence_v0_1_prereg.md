# Exp073DP — WW exact-adapter small-NSIDE equivalence v0.1

Frozen 2026-09-05 after independently validated Exp073DO static PASS and before any full-resolution WW_S0_S0 production output exists.

Scope: hosted synthetic implementation qualification `+0/+0` only. No WW scientific authority, physical support, covariance, nuisance, relation/null or G8 information may be created/read.

Parent Exp073DO: run/job `33938228418 / 101230263277`, artifact `9960883461`, digest `sha256:53e66714727fac20c3d69cda893e75aecb3e1357b6cd868f467418a8d1646c5a`, raw token `PASS_EXP073DO_WW_EXACT_ADAPTER_STATIC_ADMISSION_V0_1`.

## Frozen test
Use deterministic synthetic spin-2 source masks only at small NSIDE, PyMaster 2.7 lineage, and finite exact band edges. For each of three fixed synthetic masks:

1. construct exactly one spin-2 `NmtField` and reuse the same field object as both sides of an auto workspace;
2. compute stock `NmtWorkspace.compute_coupling_matrix(field,field,bin)` and stock `get_bandpower_windows()`;
3. persist that workspace to FITS;
4. run `ci/exp073do_ww_s0_s0_production_exact_adapter_v0_1.py` with `ncls=4` through the deterministic OpenMP downstream compiled with exactly `DSIR_WORKERS=8`;
5. require runtime proof `DSIR_OMP_TEAM=8`;
6. compare the entire canonical full array byte-for-byte to stock shape `[4,nb,4,nl]` using SHA256 equality and `numpy.array_equal`;
7. separately compare `selected_ee.bin` exactly to stock `reference[0,:,0,:]` with SHA256 equality and `numpy.array_equal`;
8. require maximum absolute difference exactly `0.0` for both full and selected arrays;
9. require adapter receipt `selected_semantics='wins[0,:,0,:] = EE<-EE'`, `science_gate_scored=false`, `ww_s0_s0_authority_created=false`, and mmap proof true.

No tolerance, `allclose`, rounding, ULP allowance, smoothing, preferred case or majority vote is permitted.

PASS token `PASS_EXP073DP_WW_EXACT_ADAPTER_SMALLNSIDE_EQUIVALENCE_V0_1` requires all three cases to satisfy every exact condition. Arithmetic mismatch is implementation qualification FAIL `+0/+0`, not a scientific WW failure. Dependency/build/transport failure is infrastructure `+0/+0`.

PASS authorizes only implementation/audit of the full-resolution durable A/B WW_S0_S0 driver with dedicated checkpoint namespaces. It still does not authorize home scientific execution until that driver and activation contract are prospectively audited.