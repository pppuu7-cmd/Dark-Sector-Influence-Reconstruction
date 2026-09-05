# Exp073DW — WW_S0_S0 DT-toolchain exact-equivalence closure v0.1

Status: preregistered support-only gate, accounting `+0/+0`.

## Purpose

Close a newly identified compile/runtime binding gap for the active Exp073DT `WW_S0_S0` science run. Exp073DP proved exact WW auto-field equivalence with the frozen adapter/downstream, but its hosted downstream was compiled with system GCC `-O2`. Exp073DT compiles the same downstream with the NaMaster conda toolchain at `-O0`, OpenMP-8, GSL from the same prefix.

Exp073DW repeats the already frozen Exp073DP auto-field synthetic exact-equivalence harness without changing its test data or acceptance rule, but compiles/runs the downstream using the Exp073DT numerical toolchain contract:

- conda-forge PyMaster/NaMaster 2.7;
- source SHA256 for the inherited `get_bandpower_windows` Python file `442e23eb542087566689271ad1c897d5da45f5b76e39def05b37d93b0098178f`;
- conda-prefix C compiler;
- `-O0 -std=c11 -fopenmp -DDSIR_WORKERS=8`;
- GSL/GSL CBLAS from the same conda prefix;
- `OMP_NUM_THREADS=8`, `OMP_DYNAMIC=FALSE`, nested BLAS-family threads fixed to 1.

## Frozen implementation identities

- Exp073DP exact-equivalence harness: `ci/exp073dp_ww_exact_adapter_smallnside_equivalence_v0_1.py`, blob `2c04c353d357c6e84709e04946e3c1f52380c06f`;
- WW adapter: `ci/exp073do_ww_s0_s0_production_exact_adapter_v0_1.py`, blob `d6f20600d6a206dd9fbb254b382e71a49c6b3c07`;
- shared exact adapter: `ci/exp073cv_wm_s3_production_exact_adapter_v0_1.py`, blob `dafe86086a470c852106f0d4ecccbda1d389e397`;
- OMP8 runtime wrapper: `ci/exp073cv_wm_s3_production_exact_adapter_omp8_v0_3.py`, blob `63ee393791bba43d3eabbea654efdb9d439d477e`;
- downstream: `ci/exp073by_mmap_full_mcm_downstream_omp10_v0_2.c`, blob `be4f381de4c5c043a9c0fcd107e63ef3f2079578`.

## PASS contract

Only token `PASS_EXP073DW_WW_S0_S0_DT_TOOLCHAIN_EXACT_EQUIVALENCE_V0_1` closes the compile/runtime binding gap. It requires the frozen DP harness itself to emit `PASS_EXP073DP_WW_EXACT_ADAPTER_SMALLNSIDE_EQUIVALENCE_V0_1`, with all three cases having:

- exact full-array equality;
- exact full SHA equality;
- max absolute full difference 0.0;
- exact selected EE equality and SHA equality;
- max absolute selected EE difference 0.0;
- mmap proof and semantics proof;
- no tolerance rescue.

## Authority firewall

Exp073DW never creates `WW_S0_S0` science authority. PASS only establishes that the exact numerical toolchain used by Exp073DT has a matching small-NSIDE auto-field equivalence proof. Exp073DT still requires its own terminal exact A/B science receipt.

If Exp073DW fails, any Exp073DT A/B equality is repeatability evidence only and must not be promoted to `WW_S0_S0` authority until the first-cause discrepancy is repaired prospectively.

Execution is GitHub-hosted only; no self-hosted job may be dispatched.
