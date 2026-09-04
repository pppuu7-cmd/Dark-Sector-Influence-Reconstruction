# Exp073BX v0.1 — full-MCM stock-order exact-equivalence support QA preregistration

Date frozen: 2026-09-04
Scope: DSIR only; hosted deterministic synthetic support QA.
Accounting: `+0/+0` for every outcome. No Wm_S3 authority and no Exp073BU science activation can be created.

## Prospective question

Exp073BV R1 proved the public Python wrapper/raw layout is exactly stock. Exp073BW G2 then proved that merely replacing NumPy/OpenBLAS solve with GSL 2.7 LU inside the selected/general-coupling reduction is still not exact. The next frozen question is whether a full-component `ncls=2` reconstruction that starts from the exact stock unbinned MCM and reproduces the pinned NaMaster-2.7 C operation order exactly recovers the complete stock bandpower-window tensor.

This gate intentionally begins **after** stock full unbinned-MCM construction. It does not yet prove a memory-stable way to construct the full MCM at DES scale. Its purpose is to isolate and validate the downstream full-component binning/LU/window arithmetic exactly before designing a scalable upstream implementation.

## Frozen lineage
- upstream NaMaster source: `LSSTDESC/NaMaster` tag `v2.7`, commit `24365fa59a38c15732f4f37e8b29265b75c442d5`;
- runtime PyMaster: exactly 2.7 / 2.7.x from conda-forge;
- source-audit S1: run/job `33816987697` / `100851195938`, artifact `9916910028`;
- wrapper/layout R1: run/job `33820184200` / `100860976434`, artifact `9917999087`;
- GSL selected-route G2: run/job `33820436824` / `100861744518`, artifact `9918084336`, immutable recovery `recovery/2026-09-04_exp073bw_gsl_selected_solver_g2_not_exact.md`;
- C emulator `ci/exp073bx_full_mcm_stock_order_v0_1.c`, introduction commit `bc0ea4f9f86083995a2cdd26579ab12252f2cd94`, frozen Git blob `bdfc756e83baa27319090f6aab20272f4144177e`;
- Python driver `ci/exp073bx_full_mcm_stock_order_v0_1.py`, introduction commit `513d6b950c54d1d67cd3ebe31923cdce17ad9d49`, frozen Git blob `ae0282cbbcdd298f00765d8de68545fe214cec0e`.

Any helper/runtime/source mismatch is fail-closed before numerical interpretation.

## Frozen source semantics being reproduced

For `MASTER` normalization with unit beams and `NmtBin.from_edges` equal weights/f_ell=1, reproduce the exact pinned `src/nmt_master.c` downstream order:

1. obtain the complete stock unbinned MCM through `NmtWorkspace.get_coupling_matrix()`, whose public ordering is `index = ncls * ell + icl`;
2. build the **full `ncls*nb x ncls*nb` binned MCM** with the stock nested loop order `icl_a -> icl_b -> ib2 -> ib3 -> i2/l2 -> i3/l3`, multiplying each unbinned element by the output-band `w_list` (uniform `1/nell` here), with unit beam product and f_ell ratio 1;
3. call GSL `gsl_linalg_LU_decomp` on that full binned matrix;
4. build `mat_coupled_bin` with stock loop order `icl1 -> ib1 -> i1/l1 -> icl2 -> l2`, accumulating the complete `ncls=2` unbinned rows with the same band weight;
5. call GSL `gsl_linalg_LU_invert` using the decomposition/permutation from step 3;
6. call GSL BLAS `gsl_blas_dgemm(CblasNoTrans,CblasNoTrans,1,inv_mcm,mat_coupled_bin,0,bpw_win)`;
7. emit the raw stock order `icl1 -> ib1 -> icl2 -> ell`, equivalent to complete tensor shape `[2,8,2,48]` for this frozen synthetic gate.

No selected-TE shortcut is used inside the emulator. Selected TE equality is recorded only as a derived diagnostic after complete-tensor comparison.

## Frozen synthetic domain
Exactly three deterministic weighted mask pairs, identical to Exp073BV/BW: NSIDE=16, RING, lmax=47, spin-0 x spin-2, edges `[0,4,8,12,16,24,32,40,48]`, `ncls=2`. No DES, Exp073R1 physical, historical Wm, Exp073CR/CQ/CM arrays, or Exp073BU physical numerical data may be read.

For each case, create a fresh stock workspace, evaluate stock `get_bandpower_windows()`, export the complete stock unbinned MCM, run the frozen full-component C/GSL emulator, then compare the entire canonical C-order `<f8 [2,8,2,48]` tensor by SHA256 and `numpy.array_equal`.

## Frozen classifications
- `F1_EXACT_FULL_STOCK_ORDER_EQUIVALENCE`: all three complete tensors have identical canonical SHA256 and `numpy.array_equal=true`. This validates the downstream full-component stock C/GSL operation order exactly for the frozen synthetic cases. It permits only a later prospectively frozen **memory-scalable full-component MCM/window construction QA**; it does not activate Wm_S3 science.
- `F2_FULL_STOCK_ORDER_MISMATCH`: valid lineage but any complete tensor differs exactly. Negative support result; inspect the pinned stock loop/weight/beam/f_ell/runtime representation before any scalable implementation. No tolerance rescue.
- `F3_SOURCE_LINEAGE_MISMATCH`: helper/source/runtime/GSL freeze mismatch. BLOCKED `+0/+0`, no numerical interpretation.
- `F4_INFRASTRUCTURE_INCOMPLETE`: compile/dependency/runner/software failure before a complete valid receipt. Infrastructure `+0/+0`; diagnose first causal failure prospectively.

No closeness threshold is an acceptance criterion. Any nonzero exact mismatch is F2.

## Workflow discipline
Hosted Ubuntu only. Static/freeze audit must precede execution. Install exact `namaster=2.7` and GSL 2.7, verify pinned `pymaster/workspaces.py` SHA256 `442e23eb542087566689271ad1c897d5da45f5b76e39def05b37d93b0098178f`, compile the C helper against the same conda GSL, execute the three frozen cases, and upload the complete JSON receipt. Workflow success alone is not F1/F2; raw artifact must be consumed.

No home/self-hosted runner, durable scientific checkpoint, readiness increment, or Wm_S3 authority is permitted.
