# Exp073DX — WW_S0_S1 conda-O2 cross-field exact-equivalence diagnostic v0.1

Status: preregistered diagnostic-only gate, accounting `+0/+0`.

## Trigger

Exp073DV established that for the Exp073DU synthetic `WW_S0_S1` workspace:

- Astropy `WSP_PRIMARY` as-is equals `NmtWorkspace.get_coupling_matrix()` bit-for-bit;
- transpose is wrong;
- the `-O0` conda/OpenMP downstream differs from direct PyMaster 2.7 windows only at last-bit scale (max absolute difference `1.1102230246251565e-16`), so the failure is in arithmetic execution, not FITS orientation.

Exp073DP previously obtained exact `ncls=4` auto-field equality using the same downstream source compiled at `-O2` with system GCC/GSL. Exp073DX tests whether using `-O2` under the conda numerical lineage restores exactness for the distinct-field cross workspace.

## Frozen test

Reuse the exact Exp073DV diagnostic code and geometry unchanged:

- diagnostic code blob `818d69cc76a927599b4eac7e19bea82cfd322640`;
- downstream blob `be4f381de4c5c043a9c0fcd107e63ef3f2079578`;
- PyMaster/NaMaster 2.7 source-lineage SHA256 `442e23eb542087566689271ad1c897d5da45f5b76e39def05b37d93b0098178f`;
- `NSIDE=16`, `nl=48`, spin-2 × spin-2, edges `[0,6,12,18,24,30,36,42,48]`;
- identical deterministic S0/S1 masks;
- conda-prefix compiler and GSL;
- `-O2 -std=c11 -fopenmp -DDSIR_WORKERS=2`;
- BLAS-family nested threads fixed to 1.

## Diagnostic interpretation

- `DIAG_EXP073DV_FITS_AS_IS_EXACT` under this O2 execution means the conda-O2 downstream exactly reproduces direct PyMaster windows and is therefore a candidate compile binding for a future prospectively qualified `WW_S0_S1` production route.
- `DIAG_EXP073DV_DOWNSTREAM_ARITHMETIC_MISMATCH` means O2 does not close the bitwise gap under this runtime.
- any other token remains unresolved and blocks cross-field production.

No tolerance rescue is permitted. Exp073DX never creates WW science authority and does not authorize changing or reinterpreting the active Exp073DT run.

Execution is GitHub-hosted only.
