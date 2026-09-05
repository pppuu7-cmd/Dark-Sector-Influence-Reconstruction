# Exp073DZ — WW_S0_S1 libnmt-O3 exact diagnostic v0.1

Status: preregistered diagnostic-only gate, accounting `+0/+0`, no science authority.

## Trigger

Exp073DV localized the distinct-field `WW_S0_S1` discrepancy to a last-bit arithmetic difference in the custom downstream, not FITS orientation. Exp073DX showed that conda `-O2` leaves the same `1.1102230246251565e-16` mismatch. Inspection of the frozen NaMaster 2.7 build path shows that `scripts/install_libnmt.sh` compiles libnmt with `CFLAGS ... -fopenmp -O3`, and `nmt_compute_bandpower_windows` lives in libnmt.

## Frozen test

Reuse `ci/exp073dv_ww_crossfield_fits_orientation_diagnostic_v0_1.py` blob `818d69cc76a927599b4eac7e19bea82cfd322640` unchanged, with downstream source `ci/exp073by_mmap_full_mcm_downstream_omp10_v0_2.c` blob `be4f381de4c5c043a9c0fcd107e63ef3f2079578`.

Runtime/compile contract:
- conda-forge PyMaster/NaMaster 2.7 and the same conda compiler/GSL prefix;
- `-O3 -std=c11 -fopenmp -DDSIR_WORKERS=2`;
- nested BLAS-family threads fixed to 1;
- same deterministic S0/S1 masks, `NSIDE=16`, `nl=48`, `ncls=4`, edges `[0,6,12,18,24,30,36,42,48]`;
- no tolerance rescue.

## Interpretation

`DIAG_EXP073DV_FITS_AS_IS_EXACT` is the only exactness-positive diagnostic outcome. It means matching libnmt's optimization level closes the distinct-field last-bit gap and identifies a candidate compile binding for a future prospectively qualified production route.

Any other token remains `+0/+0`, blocks promotion of this compile route, and creates no WW authority.

Execution is GitHub-hosted only and must not interact with Exp073DT self-hosted execution.
