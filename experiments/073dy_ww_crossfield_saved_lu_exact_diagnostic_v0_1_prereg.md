# Exp073DY — WW cross-field saved-LU exact diagnostic v0.1

Status: preregistered diagnostic-only gate, accounting `+0/+0`, no science authority.

## Trigger and hypothesis

Exp073DU/DV/DX established that the distinct spin-2 `S0->S1` workspace is constructed correctly and that `WSP_PRIMARY` streamed through Astropy is byte-exact to `NmtWorkspace.get_coupling_matrix()`, but the custom downstream differs from direct PyMaster 2.7 bandpower windows at last-bit scale (`max_abs_difference = 1.1102230246251565e-16`). Changing the downstream compile optimization from conda `-O0` to conda `-O2` did not change that mismatch. Exp073DW separately proved that the active Exp073DT auto-field route is exact under its own conda `-O0`, OpenMP-8 toolchain.

NaMaster writes three relevant numerical objects into each workspace FITS:

1. `WSP_PRIMARY`: the unbinned coupling matrix;
2. `MCM_BINNED`: the already LU-decomposed binned coupling matrix used by `gsl_linalg_LU_invert`;
3. `MCM_PERM`: the GSL LU permutation.

The current DSIR downstream reconstructs the binned matrix from `WSP_PRIMARY` and performs a new `gsl_linalg_LU_decomp`. The hypothesis is that this repeated binned accumulation/LU path is the source of the final-bit difference for a non-symmetric `ncls=4` cross workspace.

## Frozen diagnostic geometry

- PyMaster/NaMaster 2.7;
- deterministic distinct S0/S1 synthetic masks identical to Exp073DU/DV;
- `NSIDE=16`, `nl=48`, `ncls=4`;
- band edges `[0,6,12,18,24,30,36,42,48]`;
- spin-2 x spin-2 ordered workspace `W01=workspace(S0,S1)`;
- full window shape `[4,8,4,48]`;
- selected semantics `wins[0,:,0,:] = EE<-EE`;
- no tolerance, rounding, smoothing, averaging, or approximate-equality rescue.

## Required routes

The diagnostic must compare direct PyMaster `W01.get_bandpower_windows()` against:

- **recomputed-LU control**: the frozen DSIR downstream that rebuilds the binned MCM and LU from `WSP_PRIMARY`;
- **saved-LU route**: a new diagnostic downstream that uses the same unbinned MCM for `mat_coupled_bin`, but imports `MCM_BINNED` and `MCM_PERM` from the same immutable workspace FITS and calls only `gsl_linalg_LU_invert` + `dgemm` downstream.

The FITS extensions must be streamed/serialized without numerical transformation except explicit endian canonicalization. `MCM_BINNED` and `MCM_PERM` are diagnostic inputs from the same workspace, not historical science numerics.

## Classification

- `PASS_EXP073DY_SAVED_LU_CROSSFIELD_EXACT_V0_1` only if the saved-LU full array and selected EE are both `numpy.array_equal` to direct PyMaster, both SHA256 values match exactly, and both maximum absolute differences are exactly `0.0`.
- `DIAG_EXP073DY_SAVED_LU_STILL_LASTBIT_MISMATCH` if the saved-LU route remains finite and differs only numerically from direct output.
- any malformed shape, nonfinite value, runtime lineage failure, FITS contract failure, or unexpected result is fail-closed diagnostic failure.

The recomputed-LU control is expected to reproduce the already-observed last-bit mismatch and is recorded for comparison; it is not required to fail.

## Authority firewall

`science_gate_scored=false`, `ww_authority_created=false`, `production_route_authorized=false` for all outcomes. Even an exact saved-LU PASS only identifies a candidate prospective implementation for a separately preregistered `WW_S0_S1` qualifier and later full-resolution science gate.

Execution is GitHub-hosted only and must not dispatch or modify any self-hosted Exp073DT job.
