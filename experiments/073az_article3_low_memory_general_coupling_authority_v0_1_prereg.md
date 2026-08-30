# Exp073AZ — Article-3 low-memory general-coupling authority succession v0.1 preregistration

**Project:** Dark-Sector Influence Reconstruction (DSIR) only. RTK/RQIR excluded.  
**Classification:** prospective computational-authority succession after Exp073AQ exact repeatability FAIL.  
**Scientific-readiness effect of this experiment itself:** `+0`; strict Article-3 readiness remains `52%`.

## 1. Motivation and immutable predecessor state

Exp073AQ run `33327372191` terminated with hosted authority

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.

That FAIL is permanent and is not rescued, rounded, tolerated, averaged, majority-voted, or replaced by this experiment. Wm_S1 is not admitted under `controlled_single_thread_exact_v1`, and Wm_S2 remains blocked until a separately qualified successor authority exists.

A local diagnostic showed the stock NaMaster `NSIDE=4096` full workspace exceeds the model runtime's 4 GiB cgroup memory limit. A separate algebraic prototype showed that the desired bandpower-window operator can be reconstructed without retaining the full unbinned spin workspace.

Exp073AZ therefore tests a new authority class rather than modifying Exp073AQ:

`low_memory_general_coupling_deterministic_v1`.

## 2. Frozen physical/angular contract — unchanged

No scientific/support boundary changes:

- DES Y1 real masks only;
- `NSIDE=4096`, RING ordering;
- true ell axis `0..12287` inclusive;
- exactly the existing 39 frozen bandpowers with edges
  `0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288`;
- PyMaster/NaMaster 2.7 lineage;
- Wm selected response `TE <- TE`;
- WW selected response `EE <- EE`;
- selected canonical array `<f8 [39,12288]`;
- source count maps and lens threshold rules unchanged from `ci/exp073aa_article3_des_angular_task_runner_v0_1.py`;
- no radial-kernel/support, covariance, whitening, nuisance, quotient, relation/null, G7 or G8 read;
- Article-3 readiness fixed at 52% throughout this succession/qualification.

## 3. Frozen low-memory algebra

Let `L=12288`. Let `P` be the exact NaMaster `NmtBin.from_edges` output-binning operator for the frozen edges (uniform weight within each edge interval, `f_ell=1`), and let `Q` expand a bandpower to unit value on every ell in its frozen interval.

Only compact matrices of shape `[39,L]` or `[78,2L]` may survive between heavy coupling calls.

### 3.1 Wm spin-0 x spin-2

For the exact mask cross-spectrum `Cmask` used by stock NaMaster, compute only

`G02 = nmt.get_general_coupling_matrix(Cmask, 0, 2, 0, 2)`.

Immediately reduce

`A = P @ G02`

and release `G02` before any later heavy allocation.

The binned MASTER matrix is

`K = A @ Q`.

The selected window is

`W_TE_TE = solve(K, A)`.

No full `2L x 2L` workspace may be retained.

### 3.2 WW spin-2 x spin-2

Compute exactly two scalar general-coupling matrices, sequentially, never simultaneously:

`Gsame = nmt.get_general_coupling_matrix(Cmask, 2, 2, 2, 2)`

and

`Gflip = nmt.get_general_coupling_matrix(Cmask, 2, -2, 2, -2)`.

After each call, immediately reduce to `[39,L]`:

`Asame = P @ Gsame`, then release `Gsame`;

`Aflip = P @ Gflip`, then release `Gflip`.

Define

`Aplus  = (Asame + Aflip)/2`,

`Aminus = (Asame - Aflip)/2`.

This is the non-pure spin-2 parity decomposition corresponding to stock NaMaster blocks

`EE,EE = Aplus`, `EE,BB = Aminus`, `BB,EE = Aminus`, `BB,BB = Aplus`.

The compact EE/BB system is

`A2 = [[Aplus,Aminus],[Aminus,Aplus]]`,

`K2 = A2 @ Q2`,

where `Q2=diag(Q,Q)`.

The selected Article-3 window is the `EE output <- EE input` block of

`solve(K2,A2)`.

The EB/BE sector is algebraically disconnected from the selected EE/BB sector under this frozen non-pure isotropic-mask contract and need not be retained.

## 4. Memory rule

The route is intentionally streaming/iterative:

- at most one full scalar general-coupling matrix `[L,L]` may exist at a time;
- each such float64 matrix is approximately 1.125 GiB at `L=12288`;
- it must be reduced to `[39,L]` and deleted before the next scalar matrix is created;
- the full stock spin-2 `4L x 4L` unbinned workspace must never be allocated by the low-memory route.

Mask harmonic transforms may be performed in a separate hosted prerequisite stage and frozen as compact `Cmask[12288]` inputs to coupling replicas, so the heavy coupling stage can run below a 4-GiB memory ceiling.

## 5. Determinism and authority decomposition

The new route may become authority only through exact stage-wise reproducibility. No tolerance or rounding equivalence is authorized.

For a classifying real task, the following exact gates are required:

1. **Mask-PCL gate:** two independently executed hosted mask-PCL replicas must have identical canonical `<f8 [12288]` SHA256 and `numpy.array_equal=True`.
2. **Compact-coupling gate:** two independently executed hosted low-memory coupling replicas using the same admitted PCL must have identical canonical compact-array SHA256 and `numpy.array_equal=True` for every required compact array (`A` for Wm; `Asame` and `Aflip` for WW).
3. **Finalizer gate:** the compact authority is finalized twice in fresh processes on the same frozen finalizer job; selected `<f8 [39,12288]` outputs must be exact SHA/`array_equal` matches.
4. Only after all three gates PASS can a task receive successor authority class `low_memory_general_coupling_deterministic_v1`.

A mismatch at any exact gate is a task-specific computational repeatability FAIL for the new route. Failure before a valid comparison is infrastructure-INCOMPLETE.

## 6. Stock-NaMaster reference checks

Small/medium-resolution stock-workspace comparisons are implementation diagnostics only. They may report numerical differences, but no tolerance-based result can create authority or rescue a failed exact gate.

The algebraic implementation must reproduce the documented NaMaster general-coupling construction and the frozen MASTER binning equations. Any small-grid diagnostic is `NONCLASSIFYING_ALGORITHMIC_QA` and `+0` readiness.

## 7. First classifying task

The first real task under this succession is **Wm_S1 again**, because Exp073AQ failed and no later task may leapfrog it.

Wm_S2 remains forbidden until Wm_S1 obtains a valid successor-route PASS.

If Wm_S1 PASSes under Exp073AZ succession, later tasks remain separately classifying and must proceed in the previously frozen order:

`Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.

No batching may convert an individual task failure into a pass.

## 8. Anti-leakage firewall

Throughout Exp073AZ qualification and task authority:

- `physical_support_evaluated=false`;
- `operator_f_invalid_computed=false`;
- `retained_coordinates_evaluated=false`;
- `layer_b_evaluated=false`;
- `covariance_read=false`;
- `whitening_performed=false`;
- `nuisance_geometry_read=false`;
- `nuisance_svd_performed=false`;
- `relation_null_read=false`;
- `chi_square_read=false`;
- `p_value_read=false`;
- `G8_read=false`;
- `scientific_pass_claimed=false`.

## 9. Accounting

Even a successful low-memory Wm_S1 authority gives `+0` Article-3 readiness. The 52% barrier can only be revisited after all 14 angular authorities are assembled into the real Exp073AR successor aggregate and a real complete Exp073AS 1410-row pre-support candidate manifest exists under the frozen accounting contract.
