# Exp073DY — WW cross-field solver-backend diagnostic v0.1 preregistration

Status: PROSPECTIVELY FROZEN BEFORE OUTPUT
Scope: DSIR only. Support/diagnostic only; accounting +0/+0; no WW authority may be created.

## Motivation
Exp073DU and Exp073DW established an exact mismatch between the frozen production adapter and the official PyMaster 2.7 serialized→reloaded distinct spin-2 S0→S1 workspace. Exp073DX then established that the raw FITS `WSP_PRIMARY` matrix is exactly identical to the official reloaded `get_coupling_matrix()` matrix for W00/W01/W10/W11, and that transpose/orientation is not the cause. Therefore the next non-biasing diagnostic isolates the post-MCM solver/backend path.

## Frozen question
For the same deterministic nside=16 distinct spin-2 S0→S1 fixture and the same equal-width bins used by Exp073DW, determine whether the official reloaded bandpower windows are reproduced exactly by the explicit PyMaster/NumPy post-processing formula while the frozen GSL downstream emulator differs.

## Frozen runtime and inputs
- PyMaster/NaMaster 2.7 only.
- deterministic Exp073DW masks and S0→S1 cross workspace;
- serialize to FITS, reload with `NmtWorkspace.read_from`;
- ncls=4, nl=48, edges `[0,6,12,18,24,30,36,42,48]`;
- production adapter `ci/exp073do_ww_s0_s0_production_exact_adapter_v0_1.py` and frozen downstream C emulator `ci/exp073by_mmap_full_mcm_downstream_omp10_v0_2.c` are observational comparators only.

## Frozen observations
Record exact SHA256 and `numpy.array_equal` for:
1. official reloaded `get_bandpower_windows()`;
2. a reconstruction using the reloaded workspace's own `_bin_mcm(..., oneside=False/True)` products followed by the same official algebra `np.dot(np.linalg.inv(mcm_binned), oneside)`;
3. `np.linalg.solve(mcm_binned, oneside)` as a diagnostic alternative only;
4. frozen production adapter/GSL-emulator output.

Also record exact equality of the reconstructed binned matrix to `wr.mcm_binned`, and finite/max-absolute-difference diagnostics. No max-difference magnitude is an acceptance threshold.

## Interpretation frozen before output
- If the explicit `inv+dot` reconstruction is bitwise identical to official windows while the adapter is not, classify `SOLVER_BACKEND_LOCALIZED`: the remaining DU/DW mismatch is downstream arithmetic/backend, not FITS storage/orientation.
- If explicit `inv+dot` reconstruction is not bitwise identical to official windows, classify `POSTPROC_RECONSTRUCTION_NOT_LOCALIZED` and do not infer a backend cause.
- `solve` observations are diagnostic only and cannot rescue either classification.
- Any runtime/provenance/malformed-output problem is `INFRASTRUCTURE_FAIL +0/+0`.
- This experiment cannot create WW_S0_S0 or WW_S0_S1 scientific authority.
- No tolerance, allclose, rounding, smoothing, averaging, or post-hoc permutation rescue is permitted.

## Next-action rule
Only after consuming the immutable Exp073DY artifact may a new cross-workspace adapter architecture be prospectively designed. If `SOLVER_BACKEND_LOCALIZED`, the next architecture must preserve the official PyMaster 2.7 post-processing arithmetic/backend semantics rather than modifying scientific arithmetic or acceptance criteria.
